#
# spec file for package pass-otp
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           pass-otp
Version:        1.2.0
Release:        0
Summary:        A pass extension for managing one-time-password (OTP) tokens
License:        GPL-3.0-or-later
Group:          Productivity/Other
URL:            https://github.com/tadfisher/pass-otp
Source0:        https://github.com/tadfisher/pass-otp/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         fix-shebang.patch
BuildRequires:  gcc
BuildRequires:  make
Requires:       oath-toolkit
Requires:       password-store
Requires:       qrencode
BuildArch:      noarch

%description
A pass extension for managing one-time-password (OTP) tokens.
More information may be found in the pass-otp(1) man page.

%prep
%setup -q
%patch0 -p1

%build

%install
%make_install LIBDIR=%{_libexecdir}
install -Dpm 0644 %{buildroot}%{_sysconfdir}/bash_completion.d/pass-otp \
  %{buildroot}%{_datadir}/bash-completion/completions/pass-otp
rm %{buildroot}%{_sysconfdir}/bash_completion.d/pass-otp

%files
%{_mandir}/man?/%{name}.?%{ext_man}
%doc CHANGELOG.md README.md
%license LICENSE
%{_libexecdir}/password-store
%{_datadir}/bash-completion/completions/pass-otp

%changelog
