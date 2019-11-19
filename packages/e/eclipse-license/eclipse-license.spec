#
# spec file for package eclipse-license
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global eplv2_ver 2.0.1
%global eplv2_tag org.eclipse.license-license-%{eplv2_ver}.v20180423-1114
%global eplv1_ver 1.0.1
%global eplv1_tag org.eclipse.license-license-%{eplv1_ver}.v20140414-1359
Name:           eclipse-license
Version:        %{eplv2_ver}
Release:        0
Summary:        Shared license features for Eclipse
License:        EPL-1.0 AND EPL-2.0
Group:          Development/Libraries/Java
URL:            https://wiki.eclipse.org/CBI
Source1:        http://git.eclipse.org/c/cbi/org.eclipse.license.git/snapshot/%{eplv1_tag}.tar.xz
Source2:        http://git.eclipse.org/c/cbi/org.eclipse.license.git/snapshot/%{eplv2_tag}.tar.xz
BuildRequires:  tycho-bootstrap
#!BuildIgnore:  tycho
BuildArch:      noarch

%description
Shared license features for Eclipse. Other features may consume these
features to avoid unnecessary duplication of license boiler plate.

%package -n %{name}1
Version:        %{eplv1_ver}
Summary:        Shared EPL v1.0 license feature for Eclipse
License:        EPL-1.0
Provides:       eclipse-license = %{eplv1_ver}

%description -n %{name}1
Shared license feature for Eclipse. Other features may consume this
feature to avoid unnecessary duplication of license boiler plate.

%package -n %{name}2
Version:        %{eplv2_ver}
Summary:        Shared EPL v2.0 license feature for Eclipse
License:        EPL-2.0

%description -n %{name}2
Shared license feature for Eclipse. Other features may consume this
feature to avoid unnecessary duplication of license boiler plate.

%prep
%setup -q -c -T

tar xf %{SOURCE1}
tar xf %{SOURCE2}

%pom_remove_plugin ":tycho-packaging-plugin" */pom.xml

%build
pushd %{eplv1_tag}
%{mvn_build} -j
popd

pushd %{eplv2_tag}
sed -i -e 's/\(-SNAPSHOT\|\.qualifier\)/.v20180423-1114/' pom.xml */*.xml
%{mvn_build} -j
popd

%install
pushd %{eplv1_tag}
%{mvn_package} "::pom::" __noinstall
%{mvn_package} ":" 1
%mvn_install
popd

# Remove exploded tycho external bundles zipfile in case we are operating
# in bootstrap mode
rm -rf /tmp/tycho-bundles-external*

pushd %{eplv2_tag}
%{mvn_package} "::pom::" __noinstall
%{mvn_package} ":" 2
%mvn_install
popd

%files -n %{name}1 -f %{eplv1_tag}/.mfiles-1
%license %{eplv1_tag}/org.eclipse.license/*.html

%files -n %{name}2 -f %{eplv2_tag}/.mfiles-2
%license %{eplv2_tag}/org.eclipse.license/*.html

%changelog
