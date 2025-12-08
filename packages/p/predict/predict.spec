#
# spec file for package predict
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           predict
Version:        2.3.1
Release:        0
Summary:        Satellite tracking and orbital prediction
License:        GPL-2.0-or-later
URL:            https://www.qsl.net/kd2bd/predict.html
Source:         https://www.qsl.net/kd2bd/%{name}-%{version}.tar.gz
Patch0:         predict-mkdir-fix.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(ncurses)

%description
PREDICT is a multi-user satellite tracking and orbital prediction program.
Beyond displaying data, it can operate antenna rotators.

%prep
%autosetup -p1

%build
echo "char *predictpath={\"%{_datadir}/predict/\"}, soundcard=1, *version={\"%{version}\"};" > predict.h
# %%configure does too much
./build

%install
install -D -m755 predict -t %{buildroot}/%{_bindir}
install -D -m755 xpredict -t %{buildroot}/%{_bindir}
install -D -m755 kepupdate -t %{buildroot}/%{_bindir}
install -D -m644 docs/man/predict.1 -t %{buildroot}%{_mandir}/man1/
install -D -m644 default/predict.db -t %{buildroot}%{_datadir}/%{name}/default
install -D -m644 default/predict.qth -t %{buildroot}%{_datadir}/%{name}/default
install -D -m644 default/predict.tle -t %{buildroot}%{_datadir}/%{name}/default
install -D -m644 vocalizer/*.wav -t %{buildroot}%{_datadir}/%{name}/vocalizer

%files
%license COPYING LICENSE
%doc NEWS README CHANGES CREDITS HISTORY
%{_bindir}/%{name}
%{_bindir}/kepupdate
%{_bindir}/xpredict
%{_mandir}/man1/predict.1%{?ext_man}
%{_datadir}/%{name}

%changelog
