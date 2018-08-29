{
	variables: {
		rm      : '<!(node -e "require(\'addon-tools-raub\').rm()")',
		rem     : '<!(node -e "require(\'.\').rem()")',
		'XALL%' : 'false',
	},
	targets: [
		{
			target_name : 'symlinks',
			type        : 'none',
			conditions  : [[
				'OS=="linux"', {
					actions: [
						{
							action_name : 'Providing libfreeimage.so.3 x32 symlink.',
							inputs      : [],
							outputs     : ['bin-linux32'],
							action      : ['ln', '-sf', 'libfreeimage.so', 'bin-linux32/libfreeimage.so.3'],
						},
						{
							action_name : 'Providing libfreeimage.so.3 x64 symlink.',
							inputs      : [],
							outputs     : ['bin-linux64'],
							action      : ['ln', '-sf', 'libfreeimage.so', 'bin-linux64/libfreeimage.so.3'],
						},
					],
				},
			]],
		},
		{
			target_name : 'remove_extras',
			type        : 'none',
			conditions  : [[
				'XALL=="false"', {
					actions: [{
						action_name : 'Unnecessary binaries removed.',
						inputs      : [],
						outputs     : ['build'],
						action      : ['<(rm)', '-rf', '<@(rem)'],
					}],
				},
			]],
		},
	]
}
