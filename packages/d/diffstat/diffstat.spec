#
# spec file for package diffstat
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


Name:           diffstat
Version:        1.65
Release:        0
Summary:        Utility That Provides Statistics Based on the Output of diff
License:        MIT
Group:          Productivity/Text/Utilities
URL:            https://dickey.his.com/diffstat/diffstat.html
Source0:        https://invisible-mirror.net/archives/diffstat/diffstat-%{version}.tgz
Source1:        https://invisible-mirror.net/archives/diffstat/diffstat-%{version}.tgz.asc
Source2:        %{name}.keyring
Patch0:         %{name}.diff

%description
diffstat reads the output of the diff command and displays a histogram
of the insertions, deletions, and modifications in each file.

%prep
%setup -q
%patch0

%build
%configure
%make_build CFLAGS="%{optflags}"

%install
%make_install

%check
%make_build check

%files
%doc README CHANGES
%license COPYING
%{_bindir}/diffstat
%{_mandir}/man1/diffstat.1%{?ext_man}

%changelog
