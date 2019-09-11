#
# spec file for package rpmlint-mini
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           rpmlint-mini
Version:        1.10
Release:        0
Summary:        RPM file correctness checker
License:        GPL-2.0-or-later
Group:          System/Packages
Url:            http://rpmlint.zarb.org/
Source:         desktop-file-utils-0.24.tar.xz
Source100:      rpmlint-deps.txt
Source101:      rpmlint.wrapper
Source102:      rpmlint-mini.config
Source103:      polkit-default-privs.config
Source104:      appdata_checker.config
Source1000:     rpmlint-mini.rpmlintrc
# need to fetch the file from there
BuildRequires:  checkbashisms
BuildRequires:  dash
BuildRequires:  glib2-devel
BuildRequires:  glib2-devel-static
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  polkit-default-privs
BuildRequires:  polkit-whitelisting
BuildRequires:  rpmlint
#!BuildIgnore:  rpmlint-mini
Requires:       cpio

%description
rpmlint is a tool to check common errors on RPM packages. Binary and
source packages can be checked.

%prep
%setup -q -n desktop-file-utils-0.24
[ -r COPYING ]

%build
%configure
pushd src
make %{?_smp_mflags} desktop-file-validate V=1 DESKTOP_FILE_UTILS_LIBS="%{_libdir}/libglib-2.0.a -lpthread -lrt"
popd

%install
# test if the rpmlint works at all
set +e
%{_bindir}/rpmlint rpmlint
test $? -gt 0 -a $? -lt 60 && exit 1
set -e
# okay, lets put it together
mkdir -p %{buildroot}/opt/testing/share/rpmlint
install -m 755 -D src/desktop-file-validate %{buildroot}/opt/testing/bin/desktop-file-validate
cp -a %{_bindir}/dash %{_bindir}/checkbashisms %{buildroot}/opt/testing/bin
mkdir -p %{buildroot}/opt/testing/%{_lib}
cp -a %{_libdir}/libedit.so.0* %{buildroot}/opt/testing/%{_lib}
cp -a %{_datadir}/rpmlint/*.py %{buildroot}/opt/testing/share/rpmlint
# install config files
install -d -m 755 %{buildroot}/opt/testing/share/rpmlint/mini
for i in %{_sysconfdir}/rpmlint/{pie,licenses}.config "%{SOURCE103}" "%{SOURCE104}"; do
  cp $i %{buildroot}/opt/testing/share/rpmlint/mini
done
install -m 644 -D %{_datadir}/rpmlint/config %{buildroot}/opt/testing/share/rpmlint/config
install -m 644 "%{SOURCE102}" %{buildroot}/opt/testing/share/rpmlint
# extra data
install -m 755 -d %{buildroot}/opt/testing/share/rpmlint/data
install -m 644 %{_sysconfdir}/polkit-default-privs.standard %{buildroot}/opt/testing/share/rpmlint/data
install -m 644 %{_sysconfdir}/polkit-rules-whitelist.json %{buildroot}/opt/testing/share/rpmlint/data
#
pushd %{_libdir}/python%{py3_ver}/
for f in $(<%{SOURCE100}); do
  find -path "*/$f" -exec install -D {} %{buildroot}/opt/testing/%{_lib}/python%{py3_ver}/{} \;
done
# ErlangCheck dependencies that are not under %_libdir but under /usr/lib :-(
cp -a %{python3_sitelib}/{construct,pybeam,six.py} %{buildroot}/opt/testing/%{_lib}/python%{py3_ver}/site-packages
install -D %{_bindir}/python3 %{buildroot}/opt/testing/bin/python3
cp -a %{_libdir}/libpython%{py3_ver}m.so.* %{buildroot}/opt/testing/%{_lib}
cp -a %{_bindir}/rpmlint %{buildroot}/opt/testing/share/rpmlint/rpmlint.py
pushd %{buildroot}/opt/testing/share/rpmlint
PYTHONOPTIMIZE=1 python3 -O -m compileall -b *.py
rm *.py
popd
pushd %{buildroot}/opt/testing/%{_lib}/python%{py3_ver}/
PYTHONOPTIMIZE=1 find -name \*.py -exec python3 -O -m compileall -b {} \; -delete
popd
find %{buildroot}/opt/testing/ -name __pycache__  -print -exec rm -Rf {} +
rm -rf %{buildroot}/{usr,etc}
rm -f %{buildroot}/opt/testing/bin/rpmlint
install -m 755 -D %{SOURCE101} %{buildroot}/opt/testing/bin/rpmlint
# hackatlon
%define my_requires %{_builddir}/%{?buildsubdir}/%{name}-requires
cat << EOF > %{my_requires}
cat - > file.list
%{__find_requires} < file.list > requires.list
%{__find_provides} < file.list > provides.list
while read i; do
    grep -F -v "\$i" requires.list > requires.list.new
    mv requires.list.new requires.list
done < provides.list
cat requires.list
rm -f requires.list provides.list file.list
EOF
chmod +x %{my_requires}
%define _use_internal_dependency_generator 0
%define __find_requires %{my_requires}
%define __find_provides %{nil}
# final run check to detect python dep changes
LD_LIBRARY_PATH=%{buildroot}/opt/testing/%{_lib}
PYTHONPATH=%{buildroot}/opt/testing/share/rpmlint
PYTHONHOME=%{buildroot}/opt/testing/
export PYTHONPATH LD_LIBRARY_PATH PYTHONHOME
%{buildroot}/opt/testing/bin/python3 -tt -u -O %{buildroot}/opt/testing/share/rpmlint/rpmlint.pyc  /.build.binaries/*.rpm 2>&1 || exit 1
echo ".. ok"

%files
/opt/testing
%license COPYING

%changelog
