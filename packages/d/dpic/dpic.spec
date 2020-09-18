#
# spec file for package dpic
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


Name:           dpic
Version:        2020.06.01
Release:        0
Summary:        Pic language processor
License:        BSD-2-Clause AND CC-BY-3.0
Group:          Productivity/Publishing/Other
URL:            http://www.ece.uwaterloo.ca/~aplevich/dpic/
Source0:        https://ece.uwaterloo.ca/~aplevich/dpic/%{name}-%{version}.tar.gz

%description
Pic language processor for LaTeX documents or web sites.

%package        doc
Summary:        Documentation for dpic
Group:          Documentation/Other
Requires:       dpic
BuildArch:      noarch

%description    doc

This package contains the documentation for dpic.

%prep
%setup -q -n %{name}-%{version}

%build
%configure \
    --docdir=%{_docdir}/%{name}

make %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix} DOCDIR=%{buildroot}%{_docdir}/%{name}

%files
%license Copyright.txt
%doc README CHANGES
%exclude %{_docdir}/dpic/dpic-doc.pdf
%exclude %{_docdir}/dpic/dpictools.pic
%{_bindir}/%{name}
%{_mandir}/man1/dpic.1*

%files doc
%{_docdir}/dpic/dpic-doc.pdf
%{_docdir}/dpic/dpictools.pic

%changelog
