#
# spec file for package fyi
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


Name:           fyi
Version:        1.0.2
Release:        0
Summary:        notify-send alternative
License:        MIT
URL:            https://codeberg.org/dnkl/fyi
Source0:        https://codeberg.org/dnkl/fyi/archive/%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  scdoc
BuildRequires:  pkgconfig(dbus-1)

%description
FYI (for your information) is a command line utility to send desktop
notifications to the user via a notification daemon implementing XDG
desktop notifications.

%package bash-completion
Summary:        Bash completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%prep
%autosetup -n fyi

%build
%meson
%meson_build

%install
%meson_install
rm -r %{buildroot}/%{_datadir}/doc/%{name}/

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%changelog
