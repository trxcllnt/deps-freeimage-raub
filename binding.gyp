{
	'variables': {
		'rm'    : '<!(node -e "require(\'addon-tools-raub\').rm()")',
		'rem'   : '<!(node -e "require(\'.\').rem()")',
		'XALL%' : 'false',
		'l_x32' : '<!(test -d bin-linux32)',
		'l_x64' : '<!(test -d bin-linux64)',
	},
	'targets': [
		{
			'target_name' : 'symlinks',
			'type'        : 'none',
			'conditions'  : [
				[
					'OS == "linux" and l_x32', {
						'actions': [
							{
								'action_name' : 'Providing libfreeimage.so.3 x32 symlink.',
								'inputs'      : [],
								'outputs'     : ['bin-linux32'],
								'action'      : ['ln', '-sf', 'libfreeimage.so', 'bin-linux32/libfreeimage.so.3'],
							},
						],
					},
				],
				[
					'OS == "linux" and l_x64', {
						'actions': [
							{
								'action_name' : 'Providing libfreeimage.so.3 x64 symlink.',
								'inputs'      : [],
								'outputs'     : ['bin-linux64'],
								'action'      : ['ln', '-sf', 'libfreeimage.so', 'bin-linux64/libfreeimage.so.3'],
							},
						],
					},
				],
			],
		},
		{
			'target_name' : 'remove_extras',
			'type'        : 'none',
			'dependencies' : ['symlinks'],
			'conditions'  : [[
				'XALL=="false"', {
					'actions': [{
						'action_name' : 'Unnecessary binaries removed.',
						'inputs'      : [],
						'outputs'     : ['build'],
						'action'      : ['<(rm)', '-rf', '<@(rem)'],
					}],
				},
			]],
		},
	]
}
