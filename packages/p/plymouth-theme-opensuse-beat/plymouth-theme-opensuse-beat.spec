#
# spec file for package plymouth-theme-opensuse-beat
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


Name:           plymouth-theme-opensuse-beat
Version:        1.0
Release:        0
Summary:        Theme opensuse-beat for Plymouth
License:        MIT
Group:          System/Base
URL:            https://github.com/jubalh/plymouth-theme-opensuse-beat
Source:         https://github.com/jubalh/plymouth-theme-opensuse-beat/archive/%{version}.tar.gz
Requires:       plymouth-theme-script
Requires(post): plymouth-scripts
BuildArch:      noarch

%description
Theme opensuse-beat for Plymouth.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_datadir}/plymouth/themes
cp -r opensuse-beat %{buildroot}%{_datadir}/plymouth/themes

%post
if [ $1 -eq 1 ]; then
  set -x
  export LIB=%{_libdir}
  OTHEME="$(%{_sbindir}/plymouth-set-default-theme)"
  if [ "$OTHEME" = "text" ]; then
     if [ ! -e /.buildenv ]; then
       %{_sbindir}/plymouth-set-default-theme -R opensuse-beat
     else
       %{_sbindir}/plymouth-set-default-theme opensuse-beat
     fi
  fi
fi

%postun
if [ $1 -eq 0 ]; then
    export LIB=%{_libdir}
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" = "opensuse-beat" ]; then
        %{_sbindir}/plymouth-set-default-theme -R --reset
    fi
fi

%files
%license LICENSE
%doc README.md
%{_datadir}/plymouth/themes/opensuse-beat/

%changelog
