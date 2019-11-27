#
# spec file for package dreampie
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


Name:           dreampie
Version:        1.2.1
Release:        0
Summary:        Multi-pane Python shell
License:        GPL-3.0-or-later
URL:            http://www.dreampie.org/
Source:         https://github.com/noamraph/dreampie/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM https://github.com/noamraph/dreampie/pull/69
Patch0:         appdata.patch
BuildRequires:  fdupes
BuildRequires:  python-devel
BuildRequires:  update-desktop-files
Requires:       python-gtk
Requires:       python-gtksourceview
BuildArch:      noarch

%description
DreamPie is a Python shell and features a new concept for an
interactive shell: the window is divided into a history box, which
shows previous commands and their output, and a code box, where code
is written. This allows editing any amount of code, just like in an
editor, and executing it when it is ready. Code can be copied from
anywhere, edited and run instantly.

%prep
%setup -q
%patch0 -p1

%build
python setup.py build

%install
python setup.py install  --prefix=%{_prefix} --optimize=2  --root=%{buildroot} --record-rpm=filelist
cat filelist
sed -i 's/\/usr\/share\/man\/man1\/dreampie.1/\/usr\/share\/man\/man1\/dreampie.1.gz/' filelist
sed -i 's/%dir \/usr\/share\/pixmaps//' filelist
sed -i 's/%dir \/usr\/share\/applications//' filelist

%if 0%{?suse_version} == 1110
%ifarch x86_64
sed -i 's/lib64/lib/' filelist
mv %{buildroot}%{_libdir} %{buildroot}%{_prefix}/lib
%endif
%endif

cat  %{buildroot}%{_datadir}/applications/dreampie.desktop
%suse_update_desktop_file -r -u  %{buildroot}%{_datadir}/applications/dreampie.desktop Development IDE

%fdupes %{buildroot}%{python_sitelib}

%post
%desktop_database_post

%postun
%desktop_database_postun

%files -f filelist
%license dulwich/COPYING COPYING
%doc dulwich/AUTHORS dulwich/README README.md

%changelog
