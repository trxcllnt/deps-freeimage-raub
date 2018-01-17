{
	
	'variables': {
		'rem'   : '<!(node -e "console.log(require(\'.\').rem)")',
		'tools' : '<!(node -e "console.log(require(\'node-addon-tools-raub\').gypi)")',
	},
	'includes': [ '<(tools)' ],
	'targets': [
		{
			'target_name'  : 'remove_extras',
			'type'         : 'none',
			'actions'      : [
				{
					'action_name' : 'Unnecessary binaries removed.',
					'inputs'      : ['<@(rem)'],
					'outputs'     : ['build'],
					'conditions'  : [
						[ 'OS=="linux"', { 'action' : [ 'rm', '-rf', '<@(_inputs)' ] } ],
						[ 'OS=="mac"'  , { 'action' : [ 'rm', '-rf', '<@(_inputs)' ] } ],
						[ 'OS=="win"'  , { 'action' : [ '<(_rd)', '<@(_inputs)' ] } ],
					],
				}
			],
		},
		
	]
}
