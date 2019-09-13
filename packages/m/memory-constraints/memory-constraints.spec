#
# spec file for package memory-constraints
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


Name:           memory-constraints
Version:        20180406
Release:        0
Summary:        Macros to limit resources allocation when building
License:        MIT
Group:          Development/Tools/Building
URL:            https://www.opensuse.org/
Source0:        %{name}.macros
BuildRequires:  coreutils
BuildRequires:  rpm
Requires:       awk
Requires:       coreutils
BuildArch:      noarch

%description
Macros to limit various resources when building huge packages to
ensure we can produce results rather than OOM reports.

%prep
:

%build
:

%install
install -D -m 644 %{SOURCE0} %{buildroot}/%{_libexecdir}/rpm/macros.d/macros.%{name}

%files
%{_libexecdir}/rpm/macros.d/macros.%{name}

%changelog
