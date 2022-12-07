#
# spec file for package python-langtable
#
# Copyright (c) 2022 SUSE LLC
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


%define skip_python2 1
Name:           python-langtable
Version:        0.0.61
Release:        0
Summary:        Database to guess defaults for locale settings
# the translations in languages.xml and territories.xml are (mostly)
# imported from CLDR and are thus under the Unicode license, the
# short name for this license is "MIT", see:
# https://fedoraproject.org/wiki/Licensing:MIT?rd=Licensing/MIT#Modern_Style_without_sublicense_.28Unicode.29
License:        GPL-3.0-or-later
Group:          System/Localization
URL:            https://github.com/mike-fabian/langtable
Source0:        https://github.com/mike-fabian/langtable/releases/download/%{version}/langtable-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  libxml2-tools
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
langtable is used to guess reasonable defaults for locale, keyboard layout,
territory, and language, if part of that information is already known. For
example, guess the territory and the keyboard layout if the language
is known or guess the language and keyboard layout if the territory is
already known.

%prep
%autosetup -n langtable-%{version}

%build
sed -i -e "s,_DATADIR = .*,_DATADIR = '%{python3_sitelib}/langtable'," langtable/langtable.py
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
(cd langtable; python3 langtable.py)
python3 test_cases.py
for i in keyboards languages territories timezoneidparts timezones; do
    xmllint --noout --relaxng \
	langtable/schemas/$i.rng \
	langtable/data/$i.xml.gz
done

%files %{python_files}
%license COPYING unicode-license.txt
%doc README ChangeLog
%{python_sitelib}/*

%changelog
