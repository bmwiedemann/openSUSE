#
# spec file for package omemo-utils
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


Name:           omemo-utils
Version:        1.0.0
Release:        0
Summary:        Utilities for OMEMO media sharing
License:        MIT
Group:          Productivity/Networking/Instant Messenger
URL:            https://github.com/wstrm/omemo-utils
Source:         https://github.com/wstrm/omemo-utils/archive/v%{version}.tar.gz
BuildRequires:  libcurl-devel
BuildRequires:  libgcrypt-devel >= 1.7.0

%description
Utilities for OMEMO media sharing.

%prep
%setup -q

%build
%make_build PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix}

%files
%{_bindir}/omut

%changelog
