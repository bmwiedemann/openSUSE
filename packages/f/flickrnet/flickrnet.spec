#
# spec file for package flickrnet
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           flickrnet
Version:        3.5
Release:        0
Summary:        Flickr
License:        LGPL-2.1+ or CPL-1.0
Group:          Productivity/Networking/Other
Url:            http://www.codeplex.com/FlickrNet
Source:         FlickrNet3.5-Src-99196.zip
BuildRequires:  mono-devel
BuildRequires:  unzip
BuildArch:      noarch

%description
The Flickr.Net API is a .Net Library for accessing the Flickr API. Written entirely in C# it can be accessed from with any .Net language.

%package devel
Summary:        Development files for Flickr.Net
Group:          Development/Languages/Mono
Requires:       %{name} = %{version}
Requires:       pkgconfig

%description devel
The Flickr.Net API is a .NET Library for interacting with the Flickr API. It
can be accessed from any .NET language.

The %{name}-devel package contains development files for %{name}.

%prep
%setup -q -c -n FlickrNet

%build
pushd FlickrNet
xbuild FlickrNet.csproj
echo "prefix=%{_prefix}" > flickrnet.pc
echo "assemblies_dir=\${prefix}/lib/mono/flickrnet" >> flickrnet.pc
echo "Libraries=\${assemblies_dir}/FlickrNet.dll" >> flickrnet.pc
echo "Name: FlickrNet" >> flickrnet.pc
echo "Description: Flickr.Net API Library" >> flickrnet.pc
echo "Version: %{version}" >> flickrnet.pc
echo "Libs: -r:\${assemblies_dir}/FlickrNet.dll" >> flickrnet.pc
popd

%install
pushd FlickrNet
sn -v bin/Debug/FlickrNet.dll || if [[ $? = 1 ]]; then
  sn -R bin/Debug/FlickrNet.dll FlickrNet.snk
fi
gacutil -i bin/Debug/FlickrNet.dll -package flickrnet -root %{buildroot}%{_prefix}/lib
mkdir -p %{buildroot}%{_datadir}/pkgconfig
cp flickrnet.pc %{buildroot}%{_datadir}/pkgconfig/
popd

%files
%defattr(-,root,root)
%{_prefix}/lib/mono/%{name}
%{_prefix}/lib/mono/gac/FlickrNet

%files devel
%defattr(-,root,root,-)
%{_datadir}/pkgconfig/%{name}.pc

%changelog
