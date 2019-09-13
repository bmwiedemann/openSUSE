#
# spec file for package unicode-emoji
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           unicode-emoji
Version:        6.0
Release:        0
Summary:        Unicode Emoji Data Files
Group:          System/I18n/Chinese
License:        Unicode
URL:            http://www.unicode.org/emoji/
Source0:        http://www.unicode.org/copyright.html
Source1:        http://www.unicode.org/Public/emoji/%{version}/ReadMe.txt
Source2:        http://www.unicode.org/Public/emoji/%{version}/emoji-data.txt
Source3:        http://www.unicode.org/Public/emoji/%{version}/emoji-sequences.txt
Source4:        http://www.unicode.org/Public/emoji/%{version}/emoji-test.txt
Source5:        http://www.unicode.org/Public/emoji/%{version}/emoji-zwj-sequences.txt
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Unicode Emoji Data Files are the machine-readable
emoji data files associated with
http://www.unicode.org/reports/tr51/index.html

%prep

%build

%install
install -d %{buildroot}%{_datadir}/unicode/emoji
cp -p %{SOURCE0} .
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} \
%{buildroot}%{_datadir}/unicode/emoji

%files
%doc copyright.html
%dir %{_datadir}/unicode
%dir %{_datadir}/unicode/emoji
%doc %{_datadir}/unicode/emoji/ReadMe.txt
%{_datadir}/unicode/emoji/emoji-*txt

%changelog
