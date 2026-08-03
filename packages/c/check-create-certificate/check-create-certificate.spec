#
# spec file for package check-create-certificate
#
# Copyright (c) 2010-2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           check-create-certificate
Version:        0.6
Release:        0
Summary:        A non-interactive script that creates an SSL certificate if it does not exist
License:        GPL-2.0
Group:          Productivity/Networking/System
Url:            http://github.com/jdsn/check-create-certificate

Source0:        check-create-certificate
Source1:        COPYING
BuildRequires:  coreutils
Requires:       openssl >= 1.1.1
Requires:       perl
Requires:       perl-base

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
A script that checks for the existance of an SSL certificate or creates a new self signed one.
It runs non-interactively and uses either predefined values or automatically guesses the best values.

Authors:
--------
    J. Daniel Schmidt <jdsn@suse.de>

%prep

%build

%install
mkdir -p %{buildroot}%{_prefix}/sbin
install -m 755 %{SOURCE0} %{buildroot}%{_sbindir}/
mkdir -p %{buildroot}/%{_docdir}/%{name}
install -m 644 %{SOURCE1} %{buildroot}/%{_docdir}/%{name}/

%files
%defattr(-,root,root)
%attr(0755,root,root) %{_sbindir}/%{name}
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/*

%changelog
