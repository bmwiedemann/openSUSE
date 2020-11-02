#
# spec file for package stb
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           stb
Version:        2.36.1594640766.b42009b
Release:        0
Summary:        Single-File Public Domain Libraries for C/C++ 
License:        MIT OR Unlicense
Group:          Development/Libraries/C and C++
URL:            https://github.com/nothings/stb
Source0:        stb-%{version}.tar.xz
BuildRequires:  c++_compiler
BuildArch:      noarch

%description
Useful functions provided via C header files:

stb_vorbis.h                | audio            | decode ogg vorbis files from file/memory to float/16-bit signed output
stb_image.h                 | graphics         | image loading/decoding from file/memory: JPG, PNG, TGA, BMP, PSD, GIF, HDR, PIC
stb_truetype.h              | graphics         | parse, decode, and rasterize characters from truetype fonts
stb_image_write.h           | graphics         | image writing to disk: PNG, TGA, BMP
stb_image_resize.h          | graphics         | resize images larger/smaller with good quality
stb_rect_pack.h             | graphics         | simple 2D rectangle packer with decent quality
stb_sprintf.h               | utility          | fast sprintf, snprintf for C/C++
stretchy_buffer.h           | utility          | typesafe dynamic array for C (i.e. approximation to vector<>), doesn't compile as C++
stb_textedit.h              | user interface   | guts of a text editor for games etc implementing them from scratch
stb_voxel_render.h          | 3D graphics      | Minecraft-esque voxel rendering "engine" with many more features
stb_dxt.h                   | 3D graphics      | Fabian "ryg" Giesen's real-time DXT compressor
stb_perlin.h                | 3D graphics      | revised Perlin noise (3D input, 1D output)
stb_easy_font.h             | 3D graphics      | quick-and-dirty easy-to-deploy bitmap font for printing frame rate, etc
stb_tilemap_editor.h        | game dev         | embeddable tilemap editor
stb_herringbone_wang_tile.h | game dev         | herringbone Wang tile map generator
stb_c_lexer.h               | parsing          | simplify writing parsers for C-like languages
stb_divide.h                | math             | more useful 32-bit modulus e.g. "euclidean divide"
stb_connected_components.h  | misc             | incrementally compute reachability on grids
stb.h                       | misc             | helper functions for C, mostly redundant in C++; basically author's personal stuff
stb_leakcheck.h             | misc             | quick-and-dirty malloc/free leak-checking

%package devel
Summary:        Single-File Public Domain Libraries for C/C++ 
Group:          Development/Libraries/C and C++

%description devel
Useful functions provided via C header files:

stb_vorbis.h                | audio            | decode ogg vorbis files from file/memory to float/16-bit signed output
stb_image.h                 | graphics         | image loading/decoding from file/memory: JPG, PNG, TGA, BMP, PSD, GIF, HDR, PIC
stb_truetype.h              | graphics         | parse, decode, and rasterize characters from truetype fonts
stb_image_write.h           | graphics         | image writing to disk: PNG, TGA, BMP
stb_image_resize.h          | graphics         | resize images larger/smaller with good quality
stb_rect_pack.h             | graphics         | simple 2D rectangle packer with decent quality
stb_sprintf.h               | utility          | fast sprintf, snprintf for C/C++
stretchy_buffer.h           | utility          | typesafe dynamic array for C (i.e. approximation to vector<>), doesn't compile as C++
stb_textedit.h              | user interface   | guts of a text editor for games etc implementing them from scratch
stb_voxel_render.h          | 3D graphics      | Minecraft-esque voxel rendering "engine" with many more features
stb_dxt.h                   | 3D graphics      | Fabian "ryg" Giesen's real-time DXT compressor
stb_perlin.h                | 3D graphics      | revised Perlin noise (3D input, 1D output)
stb_easy_font.h             | 3D graphics      | quick-and-dirty easy-to-deploy bitmap font for printing frame rate, etc
stb_tilemap_editor.h        | game dev         | embeddable tilemap editor
stb_herringbone_wang_tile.h | game dev         | herringbone Wang tile map generator
stb_c_lexer.h               | parsing          | simplify writing parsers for C-like languages
stb_divide.h                | math             | more useful 32-bit modulus e.g. "euclidean divide"
stb_connected_components.h  | misc             | incrementally compute reachability on grids
stb.h                       | misc             | helper functions for C, mostly redundant in C++; basically author's personal stuff
stb_leakcheck.h             | misc             | quick-and-dirty malloc/free leak-checking


%prep
%setup -q

%build
# nothing to do

%install
mkdir -p %buildroot%_includedir/stb
install -m0644 *.h %buildroot%_includedir/stb
# stb_vorbis.c is a header file..
cp stb_vorbis.c %buildroot%_includedir/stb/stb_vorbis.h

%check
cd tests
make && ./a.out

%files devel
%doc README.md docs
%_includedir/stb

%changelog
