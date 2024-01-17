#
# spec file for package docbook-css-stylesheets
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           docbook-css-stylesheets
BuildArch:      noarch
Summary:        DocBook CSS Stylesheets
License:        MIT
Group:          Productivity/Publishing/DocBook
Version:        0.4
Release:        0
Source0:        http://www.badgers-in-foil.co.uk/projects/docbook-css/docbook-css-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Url:            http://www.badgers-in-foil.co.uk/projects/docbook-css/

%description
These cascading stylesheets allow you to view a DocBook XML document in
software that supports XML styled with CSS2, for example, a recent
Mozilla or Firefox browser. For more complex modifications of your XML
document use the DocBook XSL stylesheets.

%define INSTALL install -m755 -s
%define INSTALL_DIR install -d -m755
%define INSTALL_DATA install -m644
%define INSTALL_SCRIPT install -m755 -o root -g root
%define xml_dir %{_datadir}/xml
%define xml_mod_dir %{xml_dir}/docbook
%define xml_mod_dtd_dir %{xml_mod_dir}/dtd
%define xml_mod_custom_dir %{xml_mod_dir}/custom
%define xml_mod_style_dir %{xml_mod_dir}/stylesheet
%define xml_mod_style_prod_dir %{xml_mod_style_dir}/css

%prep
%setup -q -n docbook-css-%{version}

%build

%install
%{INSTALL_DIR} $RPM_BUILD_ROOT%{xml_mod_style_prod_dir}/%{version}
cp -a [[:lower:]]* $RPM_BUILD_ROOT%{xml_mod_style_prod_dir}/%{version}
pushd $RPM_BUILD_ROOT%{xml_mod_style_prod_dir}
ln -sf %{version} current
popd

%files
%defattr(-, root, root)
%dir %{xml_mod_style_dir}
%dir %{xml_mod_style_prod_dir}
%{xml_mod_style_prod_dir}/%{version}
%{xml_mod_style_prod_dir}/current

%changelog
