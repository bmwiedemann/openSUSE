#
# spec file for package guile-json
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


Name:           guile-json
Version:        1.2.0
Release:        0
Summary:        JSON module for Guile
License:        GPL-3.0-or-later
Group:          Development/Libraries/Other
Url:            https://savannah.nongnu.org/projects/guile-json/
Source0:        http://download.savannah.gnu.org/releases/guile-json/%{name}-%{version}.tar.gz
Source1:        http://download.savannah.gnu.org/releases/guile-json/%{name}-%{version}.tar.gz.sig
Source2:        https://savannah.nongnu.org/people/viewgpg.php?user_id=11331#/%{name}.keyring
Source1000:     guile-json-rpmlintrc
BuildRequires:  guile-devel >= 2.0.0
Requires:       guile >= 2.0.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Guile-json is JSON module for Guile. It supports parsing and building
JSON documents according to the http:://json.org specification. These
are the main features:

- Strictly complies to http://json.org specification.
- Build JSON documents programmatically via macros.
- Unicode support for strings.
- Allows JSON pretty printing.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install %{_smp_mflags} DESTDIR=%{buildroot}

%files
%defattr(-,root,root,-)
%license COPYING
%doc AUTHORS NEWS README
%{_datadir}/guile*
%{_libdir}/guile*

%changelog
