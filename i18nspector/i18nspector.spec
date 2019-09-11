#
# spec file for package i18nspector
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


Name:           i18nspector
Version:        0.25.8
Release:        0
Summary:        Tool for Checking gettext POT/PO/MO Files
License:        MIT
Group:          Development/Tools/Other
URL:            http://jwilk.net/software/i18nspector
Source0:        https://github.com/jwilk/i18nspector/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/jwilk/i18nspector/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  python3-devel >= 3.3.3
# Requires for tests.
BuildRequires:  python3-curses
BuildRequires:  python3-nose
BuildRequires:  python3-polib
BuildRequires:  python3-rply
#
Requires:       python3-polib
Requires:       python3-rply
BuildArch:      noarch
%if 0%{?suse_version} && 0%{?suse_version} < 1230
Requires:       python3 >= 3.3.3
%endif

%description
i18nspector is a tool for checking translation templates (POT), message
catalogues (PO) and compiled message catalogues (MO) files for common
problems. These files are used by the GNU gettext translation functions
and tools in many different development environments.

Checks include: incorrect or inconsistent character encoding, missing
headers, incorrect language codes and improper plural forms.

%prep
%setup -q

%build

%install
%make_install PREFIX=%{_prefix}

# Python byte compile.
cd %{buildroot}%{_datadir}/%{name}/
%py3_compile .

%check
make %{?_smp_mflags} test

%files
%license doc/LICENSE
%doc doc/changelog doc/README doc/tags.rst doc/todo
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man?/*

%changelog
