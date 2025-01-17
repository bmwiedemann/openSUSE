#
# spec file for package retry
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


Name:           retry
Version:        1737025645.819c129
Release:        0
Summary:        A simple tool for retrying command executions in plain POSIX sh
License:        MIT
Group:          Development/Tools/Other
BuildArch:      noarch
URL:            https://github.com/okurz/retry
Source0:        %{name}-%{version}.tar.xz
Requires:       util-linux

%description
A simple tool for retrying command executions in plain POSIX sh.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_bindir}
%make_install

%check

%files
%{_bindir}/retry
%{_bindir}/count-fail-ratio

%changelog
