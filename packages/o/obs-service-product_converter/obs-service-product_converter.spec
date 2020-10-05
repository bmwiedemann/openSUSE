#
# spec file for package obs-service-product_converter
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


%define service product_converter

Name:           obs-service-%service
Version:        1.4.4
Release:        0
Summary:        An OBS source service: create product media build descriptions
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            https://github.com/openSUSE/obs-service-%{service}
Source:         %name-%{version}.tar.xz
BuildArch:      noarch
BuildRequires:  perl(XML::Structured)
Requires:       perl(XML::Structured)
# temp workaround for broken provides of obs-server
BuildRequires:  perl-XML-Structured
Requires:       perl-XML-Structured
# workaround for missing requires of perl-XML-structured
BuildRequires:  perl-XML-Parser
Requires:       perl-XML-Parser

%description
Use this product converter to create product builds for openSUSE Tumbleweed or
SLE 15.

%prep
%setup -q

%build

%install
mkdir -p %buildroot%{_prefix}/lib/obs/service
install -m 0644 *.pm product_converter.service \
   %buildroot%{_prefix}/lib/obs/service
install -m 0755 create_single_product product_converter \
   %buildroot%{_prefix}/lib/obs/service

%check
# minimal test
rm -rf test/outdir
mkdir -p test/outdir
cd test/simple_product
PERL5LIB=%buildroot%{_prefix}/lib/obs/service ../../product_converter --outdir $PWD/../outdir/ || exit 1
cd ../outdir/
for file in _multibuild  simple-cd-cd-i586_x86_64.kiwi  simple-cd-cd-i586_x86_64.kwd  simple-release.spec
do
  if [ ! -e "$file" ]; then
    echo "ERROR $file missing"
    exit 1
  fi
done

%files
%dir %{_prefix}/lib/obs
%license COPYING
%{_prefix}/lib/obs/service

%changelog
