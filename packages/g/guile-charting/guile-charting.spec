#
# spec file for package guile-charting
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


Name:           guile-charting
Version:        0.2.0
Release:        0
Summary:        Guile library for making charts
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Other
URL:            https://wingolog.org/projects/guile-charting/
Source0:        https://wingolog.org/pub/guile-charting/%{name}-%{version}.tar.gz
BuildRequires:  guile-cairo-devel
BuildRequires:  guile-devel

%description
Guile-Charting is a library to create charts and graphs in Guile. It
is thus far a hack.

%prep
%setup -q

%build
%configure
make

%install
%make_install

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files
%license COPYING COPYING.LESSER
%doc ChangeLog HACKING NEWS README
%{_infodir}/%{name}.info.gz
%{_datadir}/guile
%{_libdir}/guile

%changelog
