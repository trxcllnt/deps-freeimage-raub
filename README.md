# FreeImage binaries

This is a part of [Node3D](https://github.com/node-3d) project.

[![NPM](https://nodei.co/npm/deps-freeimage-raub.png?compact=true)](https://www.npmjs.com/package/deps-freeimage-raub)

[![Build Status](https://api.travis-ci.com/node-3d/deps-freeimage-raub.svg?branch=master)](https://travis-ci.com/node-3d/deps-freeimage-raub)
[![CodeFactor](https://www.codefactor.io/repository/github/node-3d/deps-freeimage-raub/badge)](https://www.codefactor.io/repository/github/node-3d/deps-freeimage-raub)

> npm i -s deps-freeimage-raub


## Synopsis

This dependency package is distributing **FreeImage 3.17**
binaries through **NPM** for **Node.js** addons.

* Platforms (x64): Windows, Linux, OSX.
* Library: FreeImage.
* Linking: static dll-type.


## Usage

### binding.gyp

```javascript
	'variables': {
		'freeimage_include' : '<!(node -p "require(\'deps-freeimage-raub\').include")',
		'freeimage_bin'     : '<!(node -p "require(\'deps-freeimage-raub\').bin")',
	},
	...
	'targets': [
		{
			'target_name': '...',
			
			'include_dirs': [
				'<(freeimage_include)',
				...
			],
			
			'library_dirs': [ '<(freeimage_bin)' ],
			
			'conditions': [
				
				['OS=="linux"', {
					'libraries': [
						'-Wl,-rpath,<(freeimage_bin)',
						'<(freeimage_bin)/freeimage.so',
						...
					],
				}],
				
				['OS=="mac"', {
					'libraries': [
						'-Wl,-rpath,<(freeimage_bin)',
						'<(freeimage_bin)/freeimage.dylib',
						...
					],
				}],
				
				['OS=="win"', {
					'libraries': [ 'FreeImage.lib', ... ],
				}],
				
			],
		},
```


### addon.cpp

```cpp
#include <FreeImage.h>
```

Refer to [FreeImage 3.17 docs](http://mirrors.dotsrc.org/pub/exherbo/FreeImage3170.pdf).


## Legal notice

This software uses the [FreeImage open source image library](http://freeimage.sourceforge.net).
FreeImage is legally used under the FIPL (FreeImage Public License) version.
It is explicitly stated that FreeImage can be used commercially under FIPL.

FreeImage licensing information (a COPY) is given in a [separate file](/FREEIMAGE_FIPL),
which also can be found on
[FreeImage's official web-site](http://freeimage.sourceforge.net/license.html).
The rest of this package is MIT licensed.

Windows binaries were found on the official web-site.
Unix binaries are found in
[Ubuntu Packages](https://packages.ubuntu.com/source/cosmic/freeimage).
OSX binaries are built through MAKE system with
[Travis CI matrix](https://travis-ci.com/node-3d/deps-freeimage-raub).
See Travis [config](https://github.com/node-3d/deps-freeimage-raub/blob/master/.travis.yml)
for details.
