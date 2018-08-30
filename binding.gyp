{
	'variables': {
		'rm'    : '<!(node -e "require(\'addon-tools-raub\').rm()")',
		'rem'   : '<!(node -e "require(\'.\').rem()")',
		'XALL%' : 'false',
		'l_x32' : '<!(test -d <(module_root_dir)/bin-linux32 && echo "yes" || echo "no")',
		'l_x64' : '<!(test -d <(module_root_dir)/bin-linux64 && echo "yes" || echo "no")',
	},
	'targets': [
		{
			'target_name' : 'symlinks',
			'type'        : 'none',
			'conditions'  : [
				[
					'OS == "linux" and l_x32 == "yes"', {
						'actions': [
							{
								'action_name' : 'Providing libfreeimage.so.3 x32 symlink.',
								'inputs'      : [],
								'outputs'     : ['bin-linux32/libfreeimage.so.3'],
								'action'      : ['ln', '-sf', 'libfreeimage.so', 'bin-linux32/libfreeimage.so.3'],
							},
							{
								'action_name' : 'Providing libopenjpeg.so.2 x32 symlink.',
								'inputs'      : [],
								'outputs'     : ['bin-linux32/libopenjpeg.so.2'],
								'action'      : ['ln', '-sf', 'libopenjpeg.so', 'bin-linux32/libopenjpeg.so.2'],
							},
							{
								'action_name' : 'Providing libraw.so.9 x32 symlink.',
								'inputs'      : [],
								'outputs'     : ['bin-linux32/libraw.so.9'],
								'action'      : ['ln', '-sf', 'libraw.so', 'bin-linux32/libraw.so.9'],
							},
						],
					},
				],
				[
					'OS == "linux" and l_x64 == "yes"', {
						'actions': [
							{
								'action_name' : 'Providing libfreeimage.so.3 x64 symlink.',
								'inputs'      : [],
								'outputs'     : ['bin-linux64/libfreeimage.so.3'],
								'action'      : ['ln', '-sf', 'libfreeimage.so', 'bin-linux64/libfreeimage.so.3'],
							},
							{
								'action_name' : 'Providing libopenjpeg.so.2 x64 symlink.',
								'inputs'      : [],
								'outputs'     : ['bin-linux64/libopenjpeg.so.2'],
								'action'      : ['ln', '-sf', 'libopenjpeg.so', 'bin-linux64/libopenjpeg.so.2'],
							},
							{
								'action_name' : 'Providing libraw.so.9 x64 symlink.',
								'inputs'      : [],
								'outputs'     : ['bin-linux64/libraw.so.9'],
								'action'      : ['ln', '-sf', 'libraw.so', 'bin-linux64/libraw.so.9'],
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
