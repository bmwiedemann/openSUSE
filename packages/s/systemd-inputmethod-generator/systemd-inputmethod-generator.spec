#
# spec file for package systemd-inputmethod-generator
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


Name:           systemd-inputmethod-generator
Version:        1.0.5
Release:        0
Summary:        Expose INPUT_METHOD environment variable
License:        GPL-3.0-or-later
URL:            https://github.com/openSUSE-zh/systemd-inputmethod-generator
Source:         %{name}-%{version}.tar.gz
BuildRequires:  systemd-rpm-macros
Supplements:    (systemd and inputmethod)
BuildArch:      noarch

%description
Expose INPUT_METHOD environment variable to user sessions
according to the priority settings in /etc/X11/xim.d, so
wayland sessions and systemd fcitx/ibus user services can
work.

%prep
%setup -q

%build

%install
%make_install

%files
%dir %{_systemd_user_env_generator_dir}
%dir %{_environmentdir}
%{_systemd_user_env_generator_dir}/29-inputmethod.py3
%{_environmentdir}/99-inputmethod.conf

%changelog
