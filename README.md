# node-deps-freeimage


* Platforms: win x32/x64, linux x32/x64, mac x64.
* Library: FreeImage.
* Linking: static dll-type.


## Install

`npm i -s node-deps-freeimage-raub`


## Legal notice

This software uses the [FreeImage open source image library](http://freeimage.sourceforge.net).
FreeImage is legally used under the FIPL (FreeImage Public License) version.
It is explicitly stated that FreeImage can be used commercially under FIPL.

FreeImage licensing information (a COPY) is given in a [separate file](/FREEIMAGE_FIPL),
which also can be found on
[FreeImage's official web-site](http://freeimage.sourceforge.net/license.html).
The rest of this package is MIT licensed.

Windows binaries were found on the official website.
Unix binaries are found through
[Debian Packages](https://packages.debian.org/search?searchon=sourcenames&keywords=freeimage)
and [MacOS Formulae](http://formulae.brew.sh/formula/freeimage).


## Usage

### binding.gyp

```javascript
	'variables': {
		'freeimage_include' : '<!(node -e "console.log(require(\'node-deps-freeimage-raub\').include)")',
		'freeimage_bin'     : '<!(node -e "console.log(require(\'node-deps-freeimage-raub\').bin)")',
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
						'<(freeimage_bin)/freeimage.dylib,
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
