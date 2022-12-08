#
# spec file for package unicode-ucd
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


# For other future directories from http://www.unicode.org/Public
%global unicodedir %{_datadir}/unicode
%global ucddir %{unicodedir}/ucd
Name:           unicode-ucd
Version:        15.0.0
Release:        0
Summary:        Unicode Character Database
# FIXME: use correct group, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
# FIXME: use correct group or remove it, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
License:        Unicode-TOU
Group:          System/I18n
URL:            https://www.unicode.org/ucd/
Source0:        https://www.unicode.org/Public/zipped/%{version}/UCD.zip
# http://www.unicode.org/terms_of_use.html referenced in ReadMe.txt redirects to:
Source1:        COPYING
Source2:        https://www.unicode.org/Public/zipped/%{version}/Unihan.zip
Source3:        https://www.unicode.org/Public/zipped/%{version}/ReadMe.txt
BuildRequires:  unzip
BuildArch:      noarch

%description
The Unicode Character Database (UCD) consists of a number of data files listing
Unicode character properties and related data. It also includes data files
containing test data for conformance to several important Unicode algorithms.

%package unihan
Summary:        Unicode Han Database
# for the license and dirs
# FIXME: use correct group, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
Group:          System/I18n
Requires:       %{name} = %{version}-%{release}

%description unihan
This package contains Unihan.zip which contains the data files for the Unified
Han database of Hanzi/Kanji/Hanja Chinese characters.

%prep
%setup -q -c

grep -q "%{version}" ReadMe.txt || (echo "zip file seems not %{version}" ; exit 1)

%build
%{nil}

%install
mkdir -p %{buildroot}%{ucddir}
cp -ar . %{buildroot}%{ucddir}
cp -p %{SOURCE2} %{buildroot}%{ucddir}

cp -p %{SOURCE1} %{SOURCE3} .

%files
%doc ReadMe.txt
%license COPYING
%dir %{unicodedir}
%{ucddir}
%exclude %{ucddir}/Unihan.zip

%files unihan
%{ucddir}/Unihan.zip

%changelog
