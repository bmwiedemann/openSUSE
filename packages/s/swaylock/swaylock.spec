#
# spec file for package swaylock
#
# Copyright (c) 2023 SUSE LLC
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


Name:           swaylock
Version:        v1.7.1
Release:        0
Summary:        Screen locker for Wayland
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/swaywm/%{name}
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  meson >= 0.48.0
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  scdoc
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildRequires:  pkgconfig(xkbcommon)
Suggests:       %{name}-bash-completion
Suggests:       %{name}-fish-completion
Suggests:       %{name}-zsh-completion
Conflicts:      sway < 1.0

%description
swaylock is a screen locking utility for Wayland compositors.

%package bash-completion
Summary:        Bash completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
BuildArch:      noarch
Conflicts:      sway < 1.0

%description zsh-completion
Zsh command line completion support for %{name}.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -I/usr/include/wayland"
%meson
%meson_build

%install
%meson_install
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_pam_vendordir}
mv %{buildroot}%{_sysconfdir}/pam.d/swaylock %{buildroot}%{_pam_vendordir}

%pre
# Prepare for migration to /usr/lib; save any old .rpmsave
for i in pam.d/swaylock ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done

%posttrans
# Migration to /usr/lib, restore just created .rpmsave
for i in pam.d/swaylock ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%files
%{_bindir}/swaylock
%if 0%{?suse_version} > 1500
%{_pam_vendordir}/swaylock
%else
%config %{_sysconfdir}/pam.d/swaylock
%endif
%{_mandir}/man1/swaylock.1%{?ext_man}

%files bash-completion
%dir %{_datadir}/bash-completion/
%{_datadir}/bash-completion/completions

%files fish-completion
%dir %{_datadir}/fish/
%{_datadir}/fish/vendor_completions.d/

%files zsh-completion
%dir %{_datadir}/zsh/
%{_datadir}/zsh/site-functions

%changelog
