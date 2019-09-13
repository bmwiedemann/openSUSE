#
# spec file for package python-plaso
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


%define GITHUB_version        1.5.1

Name:           python-plaso
Version:        1.5.1
Release:        0
Summary:        Plaso is a library for working with forensic timelines
License:        Apache-2.0
Group:          Development/Libraries/Python
Url:            http://plaso.kiddaland.net/
#git:		git clone https://github.com/log2timeline/plaso.git
Source:         https://github.com/log2timeline/plaso/archive/%{GITHUB_version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  pkg-config
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python-olefile
Requires:       libzmq5 > 4.1.2
Requires:       python-XlsxWriter >= 0.9.3
Requires:       python-binplist >= 0.1.4
Requires:       python-construct = 2.5.2
Requires:       python-dateutil >= 2.4.2
Requires:       python-dfwinreg
Requires:       python-dpkt
Requires:       python-efilter >= 1.1.5
Requires:       python-hachoir-core
Requires:       python-hachoir-metadata
Requires:       python-hachoir-parser >= 1.3.4
Requires:       python-pefile >= 1.2.10+139
Requires:       python-protobuf
Requires:       python-requests
Requires:       python-yara >= 3.5.0
# These are core libraries. Make sure current versions are used
Requires:       pyesedb >= 0~20150409
Requires:       pyevt >= 0~20140731
Requires:       pyevtx >= 0~20160107
Requires:       pyfvde
Requires:       pyfwsi >= 0~20150606
Requires:       pylnk >= 0~20150830
Requires:       pymsiecf >= 0~20150314
Requires:       pyolecf >= 0~20160107
Requires:       pyregf >= 0~20150315
Requires:       pyscca
Requires:       pysigscan >= 0~20150627
Requires:       python-dfVFS >= 0~20160918
Requires:       pyvshadow >= 0~20140731

# libewf newer versions than 2016-01-26 are buggy
Requires:       libewf2 = 0~20140608
Requires:       pyewf = 0~20140608

Requires:       artifacts-validator
Requires:       pybde
Requires:       pyfsntfs
Requires:       pyqcow
Requires:       pysmdev
Requires:       pysmraw
Requires:       pyvhdi
Requires:       pyvmdk

Requires:       IPython >= 1.2.1
Requires:       python-PyYAML
Requires:       python-bencode
Requires:       python-protobuf
Requires:       python-psutil
Requires:       python-pyparsing >= 2.0.3
Requires:       python-tsk >= 0~20170128
Requires:       python-tz

Recommends:     libevt-tools
Recommends:     libevtx-tools
Recommends:     libewf-tools
Recommends:     liblnk-tools
Recommends:     libmsiecf-tools
Recommends:     libolecf-tools
Recommends:     libregf-tools
Recommends:     libvshadow-tools
Recommends:     libsmdev-tools
Recommends:     libesedb-tools
Recommends:     libvhdi-tools
Recommends:     libvmdk-tools
Recommends:     sleuthkit >= 4.1.2

# for running the test suite
Recommends:     python-mock

Provides:       plaso
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Plaso (plaso langar að safna öllu) is the Python based back-end engine used by tools such as log2timeline for automatic creation of a super timelines. The goal of log2timeline (and thus plaso) is to provide a single tool that can parse various log files and forensic artifacts from computer and related systems, such as network equipment to produce a single correlated timeline. This timeline can then be easily analysed by forensic investigators/analysts, speeding up investigations by correlating the vast amount of information found on an average computer system.

%prep
%setup -q -n plaso-%GITHUB_version
for subdir in analysis cli engine filters formatters lib multi_processing parsers preprocessors serializer storage unix winnt output; do
find plaso/$subdir -name \*.py | xargs sed -i "/#!\/usr\/bin\/python/d"
done
sed -i "/#!\/usr\/bin\/env python/d" plaso/lib/objectfilter*.py
sed -i "/#!\/usr\/bin\/python/d" plaso/frontend/__init__.py 
sed -i "/#!\/usr\/bin\/python/d" plaso/frontend/frontend.py
sed -i "/#!\/usr\/bin\/python/d" plaso/__init__.py 

%build
CFLAGS="%{optflags}" python setup.py build

%install

#if openSUSE 13.1 or Leap 42.1
%if 0%{?suse_version} < 1320
# Work around python unicode bug
mv test_data/$'\303'$'\255'mynd.dd test_data/image.dd
IFS="
"; for FILE in `grep -r ímynd.dd | sed 's/:.*$//'`; do sed 's/ímynd.dd/image.dd/g' -i $FILE; done
%endif
python setup.py install --root=%{buildroot} --prefix=%{_prefix}
# Fix python-bytecode-inconsistent-mtime
pushd %{buildroot}%{python_sitelib}/plaso/
%py_compile .
for subdir in cli unix multi_processing winnt frontend lib serializer engine parsers/shared; do
pushd %{buildroot}%{python_sitelib}/plaso/$subdir
%py_compile .
popd
done
popd
# these are installed to the wrong dir by plaso
rm %{buildroot}/usr/share/doc/plaso/ACKNOWLEDGEMENTS
rm %{buildroot}/usr/share/doc/plaso/AUTHORS
rm %{buildroot}/usr/share/doc/plaso/LICENSE
rm %{buildroot}/usr/share/doc/plaso/README
%fdupes -s %{buildroot}

%check
# this would require all the "#requires" packages to be installed.  They aren't.
#python utils/check_dependencies.py

%files
%defattr(-,root,root)
%doc ACKNOWLEDGEMENTS AUTHORS LICENSE
%doc utils/check_dependencies.py
/usr/share/plaso
%{python_sitelib}/plaso-%{version}-py2.7.egg-info
%{python_sitelib}/plaso
%{_bindir}/image_export.py
%{_bindir}/log2timeline.py
%{_bindir}/pinfo.py
%{_bindir}/preg.py
%{_bindir}/psort.py

%changelog
