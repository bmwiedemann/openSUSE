#
# spec file for package nested
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2011 Izaac Zavaleta
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


%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%else
BuildArch:      noarch
%endif
Name:           nested
Version:        1.4
Release:        0
Summary:        Specialized editor for structured documents
License:        GPL-2.0+ and Apache-2.0
Group:          Productivity/Text/Editors
Url:            https://github.com/carlos-jenkins/nested
Source0:        https://github.com/carlos-jenkins/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
# PATCH-FIX-UPSTREAM reproducible.patch -- fixed copyright year for reproducible builds
Patch0:         reproducible.patch
# PATCH-FIX-UPSTREAM sort po files for reproducible builds
Patch1:         nested-1.4-reproducible-mo-file.patch
Source2:        %{name}.rpmlintrc
BuildRequires:  fdupes
BuildRequires:  python-devel
BuildRequires:  update-desktop-files
Requires:       netpbm
Requires:       python-gtk
Requires:       texlive
Requires:       texlive-latex
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} >= 1210
BuildRequires:  python-distribute
%endif

%description
Nested is a specialized editor focused on creating structured documents such as
reports, publications, presentations, books, etc. It is designed to help the user
concentrate on writing content without being distracted by format or markup.
It offers a rich WYSIWYM interface where the user writes plain text with a
lightweight markup language.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
mkdir -p %{buildroot}%{_datadir}/applications/
cp %{SOURCE1} %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_datadir}/pixmaps/
python l10n/compile_mo.py
mkdir -p %{buildroot}%{_datadir}/locale
mv l10n/mo/* %{buildroot}%{_datadir}/locale
mkdir -p %{buildroot}%{_mandir}/man1
python -B %{_builddir}/%{name}-%{version}/nested/txt2tags.py --target man \
    --infile %{_builddir}/%{name}-%{version}/nested/examples/Manpage/Manpage.t2t \
    --outfile %{_builddir}/%{name}-%{version}/nested/nested.1
cp -p %{_builddir}/%{name}-%{version}/nested/nested.1 %{buildroot}%{_mandir}/man1
%if 0%{?suse_version} < 1210
cp %{buildroot}%{python_sitelib}/nested/nested.png %{buildroot}%{_datadir}/pixmaps/
%else
mv %{buildroot}%{python_sitelib}/nested/nested.png %{buildroot}%{_datadir}/pixmaps/
%endif
mv %{buildroot}%{_bindir}/nested.run %{buildroot}%{_bindir}/nested	
%suse_update_desktop_file %{buildroot}%{_datadir}/applications/%{name}.desktop
%fdupes %{buildroot}%{python_sitelib}/nested/
%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc CHANGELOG.txt LICENSE.txt
%{_bindir}/nested
%{_datadir}/applications/nested.desktop
%{_datadir}/pixmaps/nested.png
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{python_sitelib}/*
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog
