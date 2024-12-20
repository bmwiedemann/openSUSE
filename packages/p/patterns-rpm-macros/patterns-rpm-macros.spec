#
# spec file for package patterns-rpm-macros
#
# Copyright (c) 2024 SUSE LLC
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


Name:           patterns-rpm-macros
Version:        1.0
Release:        0
Summary:        RPM macros for building of patterns modules
License:        MIT
Group:          Development/Tools/Other
URL:            https://github.com/openSUSE/patterns
Source0:        macros.patterns
BuildRequires:  perl(URI::Escape)
BuildArch:      noarch

%description
This package contains SUSE RPM macros to aid creating patterns.

%prep

%build
cat %{SOURCE0} >> macros.patterns

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
install -m 644 macros.patterns %{buildroot}%{_rpmmacrodir}

%files
%defattr(-,root,root)
%{_rpmmacrodir}/macros.patterns

%changelog
