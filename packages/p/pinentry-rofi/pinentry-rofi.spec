#
# spec file for package pinentry-rofi
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


Name:           pinentry-rofi
Version:        2.1.0
Release:        0
Summary:        Rofi frontend to pinentry
License:        GPL-3.0-or-later+
URL:            https://git.sr.ht/~mcepl/pinentry-rofi
Source0:        pinentry-rofi-%{version}.tar.gz
BuildRequires:  lua
Requires:       rofi-launcher
Requires:       lua
Requires:       gpg
BuildArch:      noarch

%description
Simple pinentry gui using rofi.

It's similar in functionality as the gist and the previous
script, but on the MicroOS, where I work now, it is essential
to install as few as possible additional software, so Guile is
certainly too much.

To use pinentry-rofi with gpg-agent, you can set it as the
pinentry-program in the ~/.gnupg/gpg-agent.conf. Note that you
need to use the full path to the binary.

%prep
%setup -q -n %{name}-%{version}


%build
:

%install
install -Dm 755 pinentry-rofi.lua %{buildroot}%{_bindir}/pinentry-rofi

%check
export LANG=cs_CZ.utf8

%files
%license LICENSE
%doc README.md
%{_bindir}/pinentry-rofi

%changelog
