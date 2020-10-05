#
# spec file for package archmage
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


Name:           archmage
Version:        0.4.2.1
Release:        0
Summary:        A reader and decompiler for files in the CHM format
License:        GPL-2.0-or-later
Group:          Productivity/Archiving/Compression
URL:            https://github.com/dottedmag/archmage
Source:         https://github.com/dottedmag/archmage/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python3-beautifulsoup4
Requires:       python3-pychm
Requires:       python3-setuptools
Requires:       python3-sgmllib3k
BuildArch:      noarch

%description
arCHMage is a reader and decompiler for files in the CHM format. This is
the format used by Microsoft HTML Help, and is also known as Compiled HTML.

%prep
%autosetup

%build
echo %{version} > RELEASE-VERSION
%python_build

%install
%python_install
install -Dpm 0644 %{name}.1 \
  %{buildroot}%{_mandir}/man1/%{name}.1

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{python_sitelib}/*

%changelog
