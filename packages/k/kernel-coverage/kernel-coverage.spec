#
# spec file for package kernel-coverage
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           kernel-coverage
Version:        0.1
Release:        0
Summary:        Kernel Coverage Imageing, Galaxy Poster
License:        GPL-2.0
Group:          Development/Tools/Other
Url:            http://test.kernel.org/autotest
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}-%{version}-rpmlintrc
Patch1:         %{name}-0.1-fix-bashisms.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       gcc
Requires:       kernel-source
Requires:       lcov
Requires:       make
Requires:       perl-GD

%description
Creating the linux kernel coverage galaxy poster.

%prep
%setup
%patch1 -p1

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/lib/kernel-coverage
cp -a * $RPM_BUILD_ROOT/usr/lib/kernel-coverage
find $RPM_BUILD_ROOT/usr/lib/kernel-coverage -name "*orig" -delete

%files
%defattr(644,root,root)
%doc /usr/lib/kernel-coverage/COPYING
%doc /usr/lib/kernel-coverage/Changelog
%doc /usr/lib/kernel-coverage/README
%doc /usr/lib/kernel-coverage/README.SUSE
%doc /usr/lib/kernel-coverage/codemap/HACKING
%doc /usr/lib/kernel-coverage/codemap/README
%defattr(755,root,root)
%dir /usr/lib/kernel-coverage
%dir /usr/lib/kernel-coverage/cat
%dir /usr/lib/kernel-coverage/codemap
%dir /usr/lib/kernel-coverage/codemap/bin
%dir /usr/lib/kernel-coverage/codemap/web
%dir /usr/lib/kernel-coverage/codemap/python
%dir /usr/lib/kernel-coverage/zoom
/usr/lib/kernel-coverage/classify_nonstatics.pl                                                                                              
/usr/lib/kernel-coverage/codemap/bin/maketiles
/usr/lib/kernel-coverage/codemap/bin/rendertile
/usr/lib/kernel-coverage/codemap/python/Codemap.py
/usr/lib/kernel-coverage/codemap/python/ps.py
/usr/lib/kernel-coverage/conglomerate_functions.pl
/usr/lib/kernel-coverage/conglomerate_functions.pl_vorher
/usr/lib/kernel-coverage/extract_funcs.pl
/usr/lib/kernel-coverage/gen_makefile.sh
/usr/lib/kernel-coverage/genflat.pl
/usr/lib/kernel-coverage/make-outline.sh
/usr/lib/kernel-coverage/Makefile
/usr/lib/kernel-coverage/Makefile_working
/usr/lib/kernel-coverage/place.sh
/usr/lib/kernel-coverage/posterize
/usr/lib/kernel-coverage/rotary_arrange.sh
/usr/lib/kernel-coverage/setup_dirtree.pl
/usr/lib/kernel-coverage/tally
/usr/lib/kernel-coverage/total_area.pl
/usr/lib/kernel-coverage/zoom/make-dirs.sh
/usr/lib/kernel-coverage/zoom/make-image.sh
/usr/lib/kernel-coverage/zoom/Makefile
%defattr(644,root,root)
/usr/lib/kernel-coverage/analyze_function.c
/usr/lib/kernel-coverage/analyze_function.c.funktionierend
/usr/lib/kernel-coverage/analyze_function.h
/usr/lib/kernel-coverage/analyze_function.lex
/usr/lib/kernel-coverage/authors.ps
/usr/lib/kernel-coverage/codemap/bin/split-image.c
/usr/lib/kernel-coverage/codemap/web/circle_small_dark.png
/usr/lib/kernel-coverage/codemap/web/circle_small_dark.xcf
/usr/lib/kernel-coverage/codemap/web/phpinfo.php
/usr/lib/kernel-coverage/codemap/web/circle.png
/usr/lib/kernel-coverage/codemap/web/circle.xcf
/usr/lib/kernel-coverage/codemap/web/libfcgp.php
/usr/lib/kernel-coverage/codemap/web/arrow_right.png
/usr/lib/kernel-coverage/codemap/web/arrow_down.png
/usr/lib/kernel-coverage/codemap/web/map.php
/usr/lib/kernel-coverage/codemap/web/arrow_left.png
/usr/lib/kernel-coverage/codemap/web/circle_small.png
/usr/lib/kernel-coverage/codemap/web/circle_small.xcf
/usr/lib/kernel-coverage/codemap/web/quicklinks.php
/usr/lib/kernel-coverage/codemap/web/robots.txt
/usr/lib/kernel-coverage/codemap/web/index.php
/usr/lib/kernel-coverage/codemap/web/arrow_up.png
/usr/lib/kernel-coverage/codemap/web/arrow_up.xcf
/usr/lib/kernel-coverage/codemap/web/about.php
/usr/lib/kernel-coverage/codemap/web/zoom_out.png
/usr/lib/kernel-coverage/codemap/web/zoom_out.xcf
/usr/lib/kernel-coverage/codemap/web/samplelink.html
/usr/lib/kernel-coverage/codemap/web/samplelink2.html
/usr/lib/kernel-coverage/codemap/Makefile
/usr/lib/kernel-coverage/coverage.dat
/usr/lib/kernel-coverage/data2ps.c
/usr/lib/kernel-coverage/draw_arrangement.c
/usr/lib/kernel-coverage/linux-2.6.22-gcov.patch.gz
/usr/lib/kernel-coverage/function2ps.c
/usr/lib/kernel-coverage/key.ps
/usr/lib/kernel-coverage/net-ring2.ps
/usr/lib/kernel-coverage/rmclutter.c
/usr/lib/kernel-coverage/rmclutter.c.funktioniered
/usr/lib/kernel-coverage/rmclutter.lex
/usr/lib/kernel-coverage/title-template.ps
/usr/lib/kernel-coverage/tux.ps
/usr/lib/kernel-coverage/zoom/split-image.c

%changelog
