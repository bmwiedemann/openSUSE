#
# spec file for package uranium-lulzbot
#
# Copyright (c) 2025 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%{?sle15_python_module_pythons}

%if %{defined primary_python}
%define pythons python3
%define use_python     %(echo %{primary_python} | sed -e 's|python3|python3.|g')
%else
%if %{defined modern_python}
%define pythons %modern_python
%define use_python     %(echo %{modern_python} | sed -e 's|python3|python3.|g')
%else
%define pythons python311
%define use_python python3.11
%endif
%endif

Name:           uranium-lulzbot
Conflicts:      uranium
Version:        3.6.21
Release:        0
Summary:        3D printer control software: python UI stack
License:        AGPL-3.0-only
URL:            https://code.alephobjects.com/diffusion/U/uranium.git
Source0:        Uranium-%{version}.tar.xz
Patch1:         fix-build.patch
BuildRequires:  %{python_module devel}
BuildRequires:  cmake >= 3.5
BuildRequires:  gcc-c++
# The macro is called "pythons" but in our case it should only contain one python
Recommends:     %{pythons}-numpy-stl

%description
Cura is an engine for processing 3D models
into 3D printing instruction for Ultimaker and other GCode based 3D printers.
It is part of the larger open source project called "Cura".

Uranium is the Python framework for the Cura UI.

%prep
%autosetup -p1 -n Uranium-%version

%build
echo "use_python macro is set to %use_python"
CFLAGS="%{optflags}"
export CFLAGS
%cmake -DPYTHON_EXECUTABLE=/usr/bin/%{use_python} -DCMAKE_POLICY_VERSION_MINIMUM=3.5

make %{?_smp_mflags}

%install
%if 0%{?suse_version}
pushd build
%make_install
popd
%else
# Fedora
%make_install
%endif
# uranium uses i18n instead of locale for the path to translation files,
# thus we cannot use %%find_lang
find %{buildroot}%{_datadir}/uranium -name uranium.po* -delete
echo '%defattr(644,root,root,755)' > %{name}.lang
find %{buildroot}%{_datadir}/uranium -name uranium.mo | sed '
  s:'%{buildroot}'::; s:\(.*/i18n/\)\([^/]\+\)\(.*mo\):%lang(\2) \1\2\3:' \
  >> %{name}.lang
find %{buildroot}%{_datadir}/uranium -type d -path \*i18n\* | sed '
  s:'%{buildroot}'::; s:\(.*/i18n.*\):%dir \1:' \
  >> %{name}.lang
# fix cmake install dir
mv %{buildroot}/%{_datadir}/cmake* %{buildroot}/%{_datadir}/cmake

%files -f %{name}.lang
%doc docs README.md
%license LICENSE
/usr/lib/%{use_python}/site-packages/UM
%{_prefix}/lib/uranium
%dir %{_datadir}/uranium
%{_datadir}/uranium/resources
%{_datadir}/cmake

%changelog
