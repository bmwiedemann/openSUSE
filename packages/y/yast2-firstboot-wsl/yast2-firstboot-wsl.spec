#
# spec file for package yast2-firstboot-wsl
#
# Copyright (c) 2019 SUSE LLC, Nuernberg, Germany.
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


Name:           yast2-firstboot-wsl
Summary:        YaST2 firstboot settings for WSL images
License:        GPL-2.0-only
Group:          System/YaST
Version:        1
Release:        0
BuildArch:      noarch
Source0:        firstboot_write_wsl.rb
Source1:        firstboot-transform.xsl
Source10:       welcome.txt
Patch0:         yast2-firstboot-wsl.diff
Url:            https://build.opensuse.org/project/show/Virtualization:WSL
BuildRequires:  yast2-firstboot
BuildRequires:  xsltproc

%description
YaST2 firstboot settings for WSL images

%prep
%setup -Tc
cp /etc/YaST2/firstboot.xml firstboot-wsl.xml
%patch0 -p1
%if !0%{?is_opensuse}
    xsltproc "%{SOURCE1}" firstboot-wsl.xml > firstboot-wsl.xml.new
    mv firstboot-wsl.xml.new firstboot-wsl.xml
%endif
%build

%install
mkdir -p %{buildroot}/etc/YaST2
mkdir -p %{buildroot}/usr/share/YaST2/{clients,data}
#
install -m 644 firstboot-wsl.xml %{buildroot}/etc/YaST2/firstboot-wsl.xml
#
install -m 644 %{SOURCE0} %{buildroot}/usr/share/YaST2/clients
#
install -m 644 %{SOURCE10} %{buildroot}/usr/share/YaST2/data

%files
/etc/YaST2/firstboot-wsl.xml
/usr/share/YaST2

%changelog
