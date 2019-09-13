#
# spec file for package unicode-blocks
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


Name:           unicode-blocks
Version:        12.1.0
Release:        0
Summary:        Unicode Blocks Chart
License:        Unicode-DFS-2016
Group:          Productivity/Publishing/Other
URL:            http://www.unicode.org/
# Unversioned source is at http://unicode.org/Public/UNIDATA/Blocks.txt
Source:         Blocks.txt
BuildArch:      noarch

%description
Blocks from the Unicode Character Database.

%prep
%setup -q -T -c %{name}-%{version}

%build

%install
install -Dpm 0644 %{SOURCE0} \
  %{buildroot}%{_datadir}/unicode/Blocks.txt

%files
%dir %{_datadir}/unicode
%{_datadir}/unicode/Blocks.txt

%changelog
