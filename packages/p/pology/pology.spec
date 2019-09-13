#
# spec file for package pology
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pology
Version:        0.12
Release:        0
Summary:        Command-line tools for in-depth processing of PO files
License:        GPL-3.0+
Group:          Development/Tools/Other
Url:            http://pology.nedohodnik.net/
Source0:        http://pology.nedohodnik.net/release/%{name}-%{version}.tar.bz2
BuildRequires:  cmake
BuildRequires:  gettext-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  python-xml
Recommends:     aspell
Recommends:     git
Recommends:     hunspell
Recommends:     python-dbus-python
Recommends:     python-pyenchant
Recommends:     subversion
BuildArch:      noarch

%description
Pology is a Python library and collection of command-line tools for in-depth
processing of PO files, the translation file format of the GNU Gettext software
translation system. Pology functionality ranges from precision operations on
individual PO messages, to cross-file operations on large collections of PO
files.

%lang_package

%prep
%setup -q
sed -i \
    -e 's:${DATA_INSTALL_DIR}/${srcsubdir}:%{_sysconfdir}/bash_completion.d/:' \
    completion/bash/CMakeLists.txt

%build
%cmake
make -j1

%install
%cmake_install

%find_lang %{name} || echo -n >> %{name}.lang

# docs are better updated online
rm -rf %{buildroot}%{_datadir}/doc/pology/

%files
%{_bindir}/*
%{_sysconfdir}/bash_completion.d/%{name}
%{python_sitelib}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

%files lang -f %{name}.lang

%changelog
