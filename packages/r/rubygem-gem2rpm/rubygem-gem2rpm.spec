#
# spec file for package rubygem-gem2rpm
#
# Copyright (c) 2024 SUSE LLC
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


%bcond_without  gem2rpm_bootstrap
%if 0%{?suse_version} && 0%{?suse_version} < 1315
%bcond_with     ruby18
%bcond_with     ruby19
%bcond_with     ruby20
%endif
%bcond_with     ruby21
%if ! (0%{?suse_version} == 1315)
%bcond_with     ruby22
%bcond_with     ruby23
%bcond_with     ruby24
%endif
%bcond_with     ruby25
%if ! (0%{?suse_version} == 1550)
%bcond_with     ruby26
%endif
%bcond_with     ruby27
%bcond_with     ruby30
%bcond_with     ruby31
%bcond_with     ruby32
%bcond_with     ruby33
%bcond_with     ruby34
%bcond_with     rubinius25

Name:           rubygem-gem2rpm
Version:        0.10.1
Release:        0
%define mod_name gem2rpm
%define mod_full_name %{mod_name}-%{version}
%define mod_branch -%{version}
%define mod_weight 1001
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
%if %{with gem2rpm_bootstrap}
#!BuildIgnore:  rubygem(gem2rpm) rubygem(ruby:2.1.0:gem2rpm) rubygem(ruby:2.2.0:gem2rpm) rubygem(rbx:2.2:gem2rpm)
%else
BuildRequires:  %{rubygem gem2rpm}
%endif
BuildRequires:  ruby-common >= 3.2
BuildRequires:  update-alternatives
URL:            https://github.com/lutter/gem2rpm/
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        update-suse-patch.sh
Source2:        gem2rpm-opensuse
Source3:        series
Patch01:        suse.patch
Summary:        Generate rpm specfiles from gems
License:        GPL-2.0-or-later
Group:          Development/Languages/Ruby

%description
Generate source rpms and rpm spec files from a Ruby Gem.
The spec file tries to follow the gem as closely as possible

%prep
%gem_unpack
%autopatch -p1

%build
perl -p -i -e 's|("templates/opensuse.spec.erb".freeze)|$1, "templates/gem_packages.spec.erb".freeze|g' *gemspec
%gem_build

%install
%gem_install -f -N --symlink-binaries --doc-files="AUTHORS LICENSE README"
for i in %{buildroot}%{_docdir}/*rubygem-gem2rpm*/ ; do
  install -m 0644 gem2rpm-%{version}/gem2rpm.yml.documentation $i/gem2rpm.yml
done

%if %{with gem2rpm_bootstrap}
%if %{with ruby21}
%package -n ruby2.1-rubygem-gem2rpm
Summary:        Generate rpm specfiles from gems
Group:          Development/Languages/Ruby
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description -n ruby2.1-rubygem-gem2rpm
Generate source rpms and rpm spec files from a Ruby Gem.
The spec file tries to follow the gem as closely as possible

%package -n ruby2.1-rubygem-gem2rpm-doc
Summary:        RDoc documentation for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       ruby2.1-rubygem-gem2rpm = %{version}

%description -n ruby2.1-rubygem-gem2rpm-doc
Documentation generated at gem installation time.
Usually in RDoc and RI formats.

%post -n ruby2.1-rubygem-gem2rpm
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm         gem2rpm         %{_bindir}/gem2rpm.ruby2.1-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm-%{version}   gem2rpm-%{version}   %{_bindir}/gem2rpm.ruby2.1-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm.ruby2.1 gem2rpm.ruby2.1 %{_bindir}/gem2rpm.ruby2.1-%{version} %{mod_weight}

%preun -n ruby2.1-rubygem-gem2rpm
if [ "$1" = 0 ] ; then
    /usr/sbin/update-alternatives --remove gem2rpm          %{_bindir}/gem2rpm.ruby2.1-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm-%{version}    %{_bindir}/gem2rpm.ruby2.1-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm.ruby2.1  %{_bindir}/gem2rpm.ruby2.1-%{version}
fi

%files -n ruby2.1-rubygem-gem2rpm
%defattr(-,root,root,-)
%{_docdir}/ruby2.1-rubygem-gem2rpm
#{_bindir}/gem2rpm-opensuse
%{_bindir}/gem2rpm.ruby2.1-%{version}
%ghost %{_bindir}/gem2rpm.ruby2.1
%ghost %{_bindir}/gem2rpm-%{version}
%ghost %{_bindir}/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm.ruby2.1
%ghost %{_sysconfdir}/alternatives/gem2rpm-%{version}
# cache file
%{_libdir}/ruby/gems/2.1.0/cache/gem2rpm-%{version}.gem
%{_libdir}/ruby/gems/2.1.0/gems/gem2rpm-%{version}
%{_libdir}/ruby/gems/2.1.0/specifications/gem2rpm-%{version}.gemspec

%if %{with docs}
%files -n ruby2.1-rubygem-gem2rpm-doc
%defattr(-,root,root,-)
%doc %{_libdir}/ruby/gems/2.1.0/doc/gem2rpm-%{version}
%endif
%endif

%if %{with ruby18}
%package -n ruby1.8-rubygem-gem2rpm
Summary:        Generate rpm specfiles from gems
Group:          Development/Languages/Ruby
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description -n ruby1.8-rubygem-gem2rpm
Generate source rpms and rpm spec files from a Ruby Gem.
The spec file tries to follow the gem as closely as possible

%package -n ruby1.8-rubygem-gem2rpm-doc
Summary:        RDoc documentation for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       ruby1.8-rubygem-gem2rpm = %{version}

%description -n ruby1.8-rubygem-gem2rpm-doc
Documentation generated at gem installation time.
Usually in RDoc and RI formats.

%post -n ruby1.8-rubygem-gem2rpm
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm         gem2rpm         %{_bindir}/gem2rpm.ruby1.8-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm-%{version}   gem2rpm-%{version}   %{_bindir}/gem2rpm.ruby1.8-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm.ruby1.8 gem2rpm.ruby1.8 %{_bindir}/gem2rpm.ruby1.8-%{version} %{mod_weight}

%preun -n ruby1.8-rubygem-gem2rpm
if [ "$1" = 0 ] ; then
    /usr/sbin/update-alternatives --remove gem2rpm          %{_bindir}/gem2rpm.ruby1.8-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm-%{version}    %{_bindir}/gem2rpm.ruby1.8-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm.ruby1.8  %{_bindir}/gem2rpm.ruby1.8-%{version}
fi

%files -n ruby1.8-rubygem-gem2rpm
%defattr(-,root,root,-)
%{_docdir}/ruby1.8-rubygem-gem2rpm
#{_bindir}/gem2rpm-opensuse
%{_bindir}/gem2rpm.ruby1.8-%{version}
%ghost %{_bindir}/gem2rpm.ruby1.8
%ghost %{_bindir}/gem2rpm-%{version}
%ghost %{_bindir}/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm.ruby1.8
%ghost %{_sysconfdir}/alternatives/gem2rpm-%{version}
# cache file
%{_libdir}/ruby/gems/1.8/cache/gem2rpm-%{version}.gem
%{_libdir}/ruby/gems/1.8/gems/gem2rpm-%{version}
%{_libdir}/ruby/gems/1.8/specifications/gem2rpm-%{version}.gemspec

%if %{with docs}
%files -n ruby1.8-rubygem-gem2rpm-doc
%defattr(-,root,root,-)
%doc %{_libdir}/ruby/gems/1.8/doc/gem2rpm-%{version}
%endif
%endif

%if %{with ruby19}
%package -n ruby1.9-rubygem-gem2rpm
Summary:        Generate rpm specfiles from gems
Group:          Development/Languages/Ruby
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description -n ruby1.9-rubygem-gem2rpm
Generate source rpms and rpm spec files from a Ruby Gem.
The spec file tries to follow the gem as closely as possible

%package -n ruby1.9-rubygem-gem2rpm-doc
Summary:        RDoc documentation for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       ruby1.9-rubygem-gem2rpm = %{version}

%description -n ruby1.9-rubygem-gem2rpm-doc
Documentation generated at gem installation time.
Usually in RDoc and RI formats.

%post -n ruby1.9-rubygem-gem2rpm
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm         gem2rpm         %{_bindir}/gem2rpm.ruby1.9-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm-%{version}   gem2rpm-%{version}   %{_bindir}/gem2rpm.ruby1.9-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm.ruby1.9 gem2rpm.ruby1.9 %{_bindir}/gem2rpm.ruby1.9-%{version} %{mod_weight}

%preun -n ruby1.9-rubygem-gem2rpm
if [ "$1" = 0 ] ; then
    /usr/sbin/update-alternatives --remove gem2rpm          %{_bindir}/gem2rpm.ruby1.9-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm-%{version}    %{_bindir}/gem2rpm.ruby1.9-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm.ruby1.9  %{_bindir}/gem2rpm.ruby1.9-%{version}
fi

%files -n ruby1.9-rubygem-gem2rpm
%defattr(-,root,root,-)
%{_docdir}/ruby1.9-rubygem-gem2rpm
#{_bindir}/gem2rpm-opensuse
%{_bindir}/gem2rpm.ruby1.9-%{version}
%ghost %{_bindir}/gem2rpm.ruby1.9
%ghost %{_bindir}/gem2rpm-%{version}
%ghost %{_bindir}/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm.ruby1.9
%ghost %{_sysconfdir}/alternatives/gem2rpm-%{version}
# cache file
%{_libdir}/ruby/gems/1.9.1/cache/gem2rpm-%{version}.gem
%{_libdir}/ruby/gems/1.9.1/gems/gem2rpm-%{version}
%{_libdir}/ruby/gems/1.9.1/specifications/gem2rpm-%{version}.gemspec

%if %{with docs}
%files -n ruby1.9-rubygem-gem2rpm-doc
%defattr(-,root,root,-)
%doc %{_libdir}/ruby/gems/1.9.1/doc/gem2rpm-%{version}
%endif
%endif

%if %{with ruby20}
%package -n ruby2.0-rubygem-gem2rpm
Summary:        Generate rpm specfiles from gems
Group:          Development/Languages/Ruby
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description -n ruby2.0-rubygem-gem2rpm
Generate source rpms and rpm spec files from a Ruby Gem.
The spec file tries to follow the gem as closely as possible

%package -n ruby2.0-rubygem-gem2rpm-doc
Summary:        RDoc documentation for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       ruby2.0-rubygem-gem2rpm = %{version}

%description -n ruby2.0-rubygem-gem2rpm-doc
Documentation generated at gem installation time.
Usually in RDoc and RI formats.

%post -n ruby2.0-rubygem-gem2rpm
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm         gem2rpm         %{_bindir}/gem2rpm.ruby2.0-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm-%{version}   gem2rpm-%{version}   %{_bindir}/gem2rpm.ruby2.0-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm.ruby2.0 gem2rpm.ruby2.0 %{_bindir}/gem2rpm.ruby2.0-%{version} %{mod_weight}

%preun -n ruby2.0-rubygem-gem2rpm
if [ "$1" = 0 ] ; then
    /usr/sbin/update-alternatives --remove gem2rpm          %{_bindir}/gem2rpm.ruby2.0-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm-%{version}    %{_bindir}/gem2rpm.ruby2.0-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm.ruby2.0  %{_bindir}/gem2rpm.ruby2.0-%{version}
fi

%files -n ruby2.0-rubygem-gem2rpm
%defattr(-,root,root,-)
%{_docdir}/ruby2.0-rubygem-gem2rpm
#{_bindir}/gem2rpm-opensuse
%{_bindir}/gem2rpm.ruby2.0-%{version}
%ghost %{_bindir}/gem2rpm.ruby2.0
%ghost %{_bindir}/gem2rpm-%{version}
%ghost %{_bindir}/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm.ruby2.0
%ghost %{_sysconfdir}/alternatives/gem2rpm-%{version}
# cache file
%{_libdir}/ruby/gems/2.0.0/cache/gem2rpm-%{version}.gem
%{_libdir}/ruby/gems/2.0.0/gems/gem2rpm-%{version}
%{_libdir}/ruby/gems/2.0.0/specifications/gem2rpm-%{version}.gemspec

%if %{with docs}
%files -n ruby2.0-rubygem-gem2rpm-doc
%defattr(-,root,root,-)
%doc %{_libdir}/ruby/gems/2.0.0/doc/gem2rpm-%{version}
%endif
%endif

%if %{with ruby22}
%package -n ruby2.2-rubygem-gem2rpm
Summary:        Generate rpm specfiles from gems
Group:          Development/Languages/Ruby
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description -n ruby2.2-rubygem-gem2rpm
Generate source rpms and rpm spec files from a Ruby Gem.
The spec file tries to follow the gem as closely as possible

%package -n ruby2.2-rubygem-gem2rpm-doc
Summary:        RDoc documentation for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       ruby2.2-rubygem-gem2rpm = %{version}

%description -n ruby2.2-rubygem-gem2rpm-doc
Documentation generated at gem installation time.
Usually in RDoc and RI formats.

%post -n ruby2.2-rubygem-gem2rpm
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm         gem2rpm         %{_bindir}/gem2rpm.ruby2.2-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm-%{version}   gem2rpm-%{version}   %{_bindir}/gem2rpm.ruby2.2-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm.ruby2.2 gem2rpm.ruby2.2 %{_bindir}/gem2rpm.ruby2.2-%{version} %{mod_weight}

%preun -n ruby2.2-rubygem-gem2rpm
if [ "$1" = 0 ] ; then
    /usr/sbin/update-alternatives --remove gem2rpm          %{_bindir}/gem2rpm.ruby2.2-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm-%{version}    %{_bindir}/gem2rpm.ruby2.2-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm.ruby2.2  %{_bindir}/gem2rpm.ruby2.2-%{version}
fi

%files -n ruby2.2-rubygem-gem2rpm
%defattr(-,root,root,-)
%{_docdir}/ruby2.2-rubygem-gem2rpm
#{_bindir}/gem2rpm-opensuse
%{_bindir}/gem2rpm.ruby2.2-%{version}
%ghost %{_bindir}/gem2rpm.ruby2.2
%ghost %{_bindir}/gem2rpm-%{version}
%ghost %{_bindir}/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm.ruby2.2
%ghost %{_sysconfdir}/alternatives/gem2rpm-%{version}
# cache file
%{_libdir}/ruby/gems/2.2.0/cache/gem2rpm-%{version}.gem
%{_libdir}/ruby/gems/2.2.0/gems/gem2rpm-%{version}
%{_libdir}/ruby/gems/2.2.0/specifications/gem2rpm-%{version}.gemspec

%if %{with docs}
%files -n ruby2.2-rubygem-gem2rpm-doc
%defattr(-,root,root,-)
%doc %{_libdir}/ruby/gems/2.2.0/doc/gem2rpm-%{version}
%endif
%endif

%if %{with ruby23}
%package -n ruby2.3-rubygem-gem2rpm
Summary:        Generate rpm specfiles from gems
Group:          Development/Languages/Ruby
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description -n ruby2.3-rubygem-gem2rpm
Generate source rpms and rpm spec files from a Ruby Gem.
The spec file tries to follow the gem as closely as possible

%package -n ruby2.3-rubygem-gem2rpm-doc
Summary:        RDoc documentation for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       ruby2.3-rubygem-gem2rpm = %{version}

%description -n ruby2.3-rubygem-gem2rpm-doc
Documentation generated at gem installation time.
Usually in RDoc and RI formats.

%post -n ruby2.3-rubygem-gem2rpm
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm         gem2rpm         %{_bindir}/gem2rpm.ruby2.3-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm-%{version}   gem2rpm-%{version}   %{_bindir}/gem2rpm.ruby2.3-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm.ruby2.3 gem2rpm.ruby2.3 %{_bindir}/gem2rpm.ruby2.3-%{version} %{mod_weight}

%preun -n ruby2.3-rubygem-gem2rpm
if [ "$1" = 0 ] ; then
    /usr/sbin/update-alternatives --remove gem2rpm          %{_bindir}/gem2rpm.ruby2.3-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm-%{version}    %{_bindir}/gem2rpm.ruby2.3-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm.ruby2.3  %{_bindir}/gem2rpm.ruby2.3-%{version}
fi

%files -n ruby2.3-rubygem-gem2rpm
%defattr(-,root,root,-)
%{_docdir}/ruby2.3-rubygem-gem2rpm
#{_bindir}/gem2rpm-opensuse
%{_bindir}/gem2rpm.ruby2.3-%{version}
%ghost %{_bindir}/gem2rpm.ruby2.3
%ghost %{_bindir}/gem2rpm-%{version}
%ghost %{_bindir}/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm.ruby2.3
%ghost %{_sysconfdir}/alternatives/gem2rpm-%{version}
# cache file
%{_libdir}/ruby/gems/2.3.0/cache/gem2rpm-%{version}.gem
%{_libdir}/ruby/gems/2.3.0/gems/gem2rpm-%{version}
%{_libdir}/ruby/gems/2.3.0/specifications/gem2rpm-%{version}.gemspec

%if %{with docs}
%files -n ruby2.3-rubygem-gem2rpm-doc
%defattr(-,root,root,-)
%doc %{_libdir}/ruby/gems/2.3.0/doc/gem2rpm-%{version}
%endif
%endif

%if %{with ruby24}
%package -n ruby2.4-rubygem-gem2rpm
Summary:        Generate rpm specfiles from gems
Group:          Development/Languages/Ruby
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description -n ruby2.4-rubygem-gem2rpm
Generate source rpms and rpm spec files from a Ruby Gem.
The spec file tries to follow the gem as closely as possible

%package -n ruby2.4-rubygem-gem2rpm-doc
Summary:        RDoc documentation for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       ruby2.4-rubygem-gem2rpm = %{version}

%description -n ruby2.4-rubygem-gem2rpm-doc
Documentation generated at gem installation time.
Usually in RDoc and RI formats.

%post -n ruby2.4-rubygem-gem2rpm
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm         gem2rpm         %{_bindir}/gem2rpm.ruby2.4-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm-%{version}   gem2rpm-%{version}   %{_bindir}/gem2rpm.ruby2.4-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm.ruby2.4 gem2rpm.ruby2.4 %{_bindir}/gem2rpm.ruby2.4-%{version} %{mod_weight}

%preun -n ruby2.4-rubygem-gem2rpm
if [ "$1" = 0 ] ; then
    /usr/sbin/update-alternatives --remove gem2rpm          %{_bindir}/gem2rpm.ruby2.4-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm-%{version}    %{_bindir}/gem2rpm.ruby2.4-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm.ruby2.4  %{_bindir}/gem2rpm.ruby2.4-%{version}
fi

%files -n ruby2.4-rubygem-gem2rpm
%defattr(-,root,root,-)
%{_docdir}/ruby2.4-rubygem-gem2rpm
#{_bindir}/gem2rpm-opensuse
%{_bindir}/gem2rpm.ruby2.4-%{version}
%ghost %{_bindir}/gem2rpm.ruby2.4
%ghost %{_bindir}/gem2rpm-%{version}
%ghost %{_bindir}/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm.ruby2.4
%ghost %{_sysconfdir}/alternatives/gem2rpm-%{version}
# cache file
%{_libdir}/ruby/gems/2.4.0/cache/gem2rpm-%{version}.gem
%{_libdir}/ruby/gems/2.4.0/gems/gem2rpm-%{version}
%{_libdir}/ruby/gems/2.4.0/specifications/gem2rpm-%{version}.gemspec

%if %{with docs}
%files -n ruby2.4-rubygem-gem2rpm-doc
%defattr(-,root,root,-)
%doc %{_libdir}/ruby/gems/2.4.0/doc/gem2rpm-%{version}
%endif
%endif

%if %{with ruby25}
%package -n ruby2.5-rubygem-gem2rpm
Summary:        Generate rpm specfiles from gems
Group:          Development/Languages/Ruby
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description -n ruby2.5-rubygem-gem2rpm
Generate source rpms and rpm spec files from a Ruby Gem.
The spec file tries to follow the gem as closely as possible

%package -n ruby2.5-rubygem-gem2rpm-doc
Summary:        RDoc documentation for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       ruby2.5-rubygem-gem2rpm = %{version}

%description -n ruby2.5-rubygem-gem2rpm-doc
Documentation generated at gem installation time.
Usually in RDoc and RI formats.

%post -n ruby2.5-rubygem-gem2rpm
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm         gem2rpm         %{_bindir}/gem2rpm.ruby2.5-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm-%{version}   gem2rpm-%{version}   %{_bindir}/gem2rpm.ruby2.5-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm.ruby2.5 gem2rpm.ruby2.5 %{_bindir}/gem2rpm.ruby2.5-%{version} %{mod_weight}

%preun -n ruby2.5-rubygem-gem2rpm
if [ "$1" = 0 ] ; then
    /usr/sbin/update-alternatives --remove gem2rpm          %{_bindir}/gem2rpm.ruby2.5-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm-%{version}    %{_bindir}/gem2rpm.ruby2.5-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm.ruby2.5  %{_bindir}/gem2rpm.ruby2.5-%{version}
fi

%files -n ruby2.5-rubygem-gem2rpm
%defattr(-,root,root,-)
%{_docdir}/ruby2.5-rubygem-gem2rpm
#{_bindir}/gem2rpm-opensuse
%{_bindir}/gem2rpm.ruby2.5-%{version}
%ghost %{_bindir}/gem2rpm.ruby2.5
%ghost %{_bindir}/gem2rpm-%{version}
%ghost %{_bindir}/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm.ruby2.5
%ghost %{_sysconfdir}/alternatives/gem2rpm-%{version}
# cache file
%{_libdir}/ruby/gems/2.5.0/cache/gem2rpm-%{version}.gem
%{_libdir}/ruby/gems/2.5.0/gems/gem2rpm-%{version}
%{_libdir}/ruby/gems/2.5.0/specifications/gem2rpm-%{version}.gemspec

%if %{with docs}
%files -n ruby2.5-rubygem-gem2rpm-doc
%defattr(-,root,root,-)
%doc %{_libdir}/ruby/gems/2.5.0/doc/gem2rpm-%{version}
%endif
%endif

%if %{with ruby26}
%package -n ruby2.6-rubygem-gem2rpm
Summary:        Generate rpm specfiles from gems
Group:          Development/Languages/Ruby
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description -n ruby2.6-rubygem-gem2rpm
Generate source rpms and rpm spec files from a Ruby Gem.
The spec file tries to follow the gem as closely as possible

%package -n ruby2.6-rubygem-gem2rpm-doc
Summary:        RDoc documentation for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       ruby2.6-rubygem-gem2rpm = %{version}

%description -n ruby2.6-rubygem-gem2rpm-doc
Documentation generated at gem installation time.
Usually in RDoc and RI formats.

%post -n ruby2.6-rubygem-gem2rpm
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm         gem2rpm         %{_bindir}/gem2rpm.ruby2.6-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm-%{version}   gem2rpm-%{version}   %{_bindir}/gem2rpm.ruby2.6-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm.ruby2.6 gem2rpm.ruby2.6 %{_bindir}/gem2rpm.ruby2.6-%{version} %{mod_weight}

%preun -n ruby2.6-rubygem-gem2rpm
if [ "$1" = 0 ] ; then
    /usr/sbin/update-alternatives --remove gem2rpm          %{_bindir}/gem2rpm.ruby2.6-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm-%{version}    %{_bindir}/gem2rpm.ruby2.6-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm.ruby2.6  %{_bindir}/gem2rpm.ruby2.6-%{version}
fi

%files -n ruby2.6-rubygem-gem2rpm
%defattr(-,root,root,-)
%{_docdir}/ruby2.6-rubygem-gem2rpm
#{_bindir}/gem2rpm-opensuse
%{_bindir}/gem2rpm.ruby2.6-%{version}
%ghost %{_bindir}/gem2rpm.ruby2.6
%ghost %{_bindir}/gem2rpm-%{version}
%ghost %{_bindir}/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm.ruby2.6
%ghost %{_sysconfdir}/alternatives/gem2rpm-%{version}
# cache file
%{_libdir}/ruby/gems/2.6.0/cache/gem2rpm-%{version}.gem
%{_libdir}/ruby/gems/2.6.0/gems/gem2rpm-%{version}
%{_libdir}/ruby/gems/2.6.0/specifications/gem2rpm-%{version}.gemspec

%if %{with docs}
%files -n ruby2.6-rubygem-gem2rpm-doc
%defattr(-,root,root,-)
%doc %{_libdir}/ruby/gems/2.6.0/doc/gem2rpm-%{version}
%endif
%endif

%if %{with ruby27}
%package -n ruby2.7-rubygem-gem2rpm
Summary:        Generate rpm specfiles from gems
Group:          Development/Languages/Ruby
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description -n ruby2.7-rubygem-gem2rpm
Generate source rpms and rpm spec files from a Ruby Gem.
The spec file tries to follow the gem as closely as possible

%package -n ruby2.7-rubygem-gem2rpm-doc
Summary:        RDoc documentation for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       ruby2.7-rubygem-gem2rpm = %{version}

%description -n ruby2.7-rubygem-gem2rpm-doc
Documentation generated at gem installation time.
Usually in RDoc and RI formats.

%post -n ruby2.7-rubygem-gem2rpm
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm         gem2rpm         %{_bindir}/gem2rpm.ruby2.7-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm-%{version}   gem2rpm-%{version}   %{_bindir}/gem2rpm.ruby2.7-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm.ruby2.7 gem2rpm.ruby2.7 %{_bindir}/gem2rpm.ruby2.7-%{version} %{mod_weight}

%preun -n ruby2.7-rubygem-gem2rpm
if [ "$1" = 0 ] ; then
    /usr/sbin/update-alternatives --remove gem2rpm          %{_bindir}/gem2rpm.ruby2.7-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm-%{version}    %{_bindir}/gem2rpm.ruby2.7-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm.ruby2.7  %{_bindir}/gem2rpm.ruby2.7-%{version}
fi

%files -n ruby2.7-rubygem-gem2rpm
%defattr(-,root,root,-)
%{_docdir}/ruby2.7-rubygem-gem2rpm
#{_bindir}/gem2rpm-opensuse
%{_bindir}/gem2rpm.ruby2.7-%{version}
%ghost %{_bindir}/gem2rpm.ruby2.7
%ghost %{_bindir}/gem2rpm-%{version}
%ghost %{_bindir}/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm.ruby2.7
%ghost %{_sysconfdir}/alternatives/gem2rpm-%{version}
# cache file
%{_libdir}/ruby/gems/2.7.0/cache/gem2rpm-%{version}.gem
%{_libdir}/ruby/gems/2.7.0/gems/gem2rpm-%{version}
%{_libdir}/ruby/gems/2.7.0/specifications/gem2rpm-%{version}.gemspec

%if %{with docs}
%files -n ruby2.7-rubygem-gem2rpm-doc
%defattr(-,root,root,-)
%doc %{_libdir}/ruby/gems/2.7.0/doc/gem2rpm-%{version}
%endif
%endif

%if %{with ruby30}
%package -n ruby3.0-rubygem-gem2rpm
Summary:        Generate rpm specfiles from gems
Group:          Development/Languages/Ruby
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description -n ruby3.0-rubygem-gem2rpm
Generate source rpms and rpm spec files from a Ruby Gem.
The spec file tries to follow the gem as closely as possible

%package -n ruby3.0-rubygem-gem2rpm-doc
Summary:        RDoc documentation for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       ruby3.0-rubygem-gem2rpm = %{version}

%description -n ruby3.0-rubygem-gem2rpm-doc
Documentation generated at gem installation time.
Usually in RDoc and RI formats.

%post -n ruby3.0-rubygem-gem2rpm
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm         gem2rpm         %{_bindir}/gem2rpm.ruby3.0-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm-%{version}   gem2rpm-%{version}   %{_bindir}/gem2rpm.ruby3.0-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm.ruby3.0 gem2rpm.ruby3.0 %{_bindir}/gem2rpm.ruby3.0-%{version} %{mod_weight}

%preun -n ruby3.0-rubygem-gem2rpm
if [ "$1" = 0 ] ; then
    /usr/sbin/update-alternatives --remove gem2rpm          %{_bindir}/gem2rpm.ruby3.0-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm-%{version}    %{_bindir}/gem2rpm.ruby3.0-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm.ruby3.0  %{_bindir}/gem2rpm.ruby3.0-%{version}
fi

%files -n ruby3.0-rubygem-gem2rpm
%defattr(-,root,root,-)
%{_docdir}/ruby3.0-rubygem-gem2rpm
#{_bindir}/gem2rpm-opensuse
%{_bindir}/gem2rpm.ruby3.0-%{version}
%ghost %{_bindir}/gem2rpm.ruby3.0
%ghost %{_bindir}/gem2rpm-%{version}
%ghost %{_bindir}/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm.ruby3.0
%ghost %{_sysconfdir}/alternatives/gem2rpm-%{version}
# cache file
%{_libdir}/ruby/gems/3.0.0/cache/gem2rpm-%{version}.gem
%{_libdir}/ruby/gems/3.0.0/gems/gem2rpm-%{version}
%{_libdir}/ruby/gems/3.0.0/specifications/gem2rpm-%{version}.gemspec

%if %{with docs}
%files -n ruby3.0-rubygem-gem2rpm-doc
%defattr(-,root,root,-)
%doc %{_libdir}/ruby/gems/3.0.0/doc/gem2rpm-%{version}
%endif
%endif

%if %{with ruby31}
%package -n ruby3.1-rubygem-gem2rpm
Summary:        Generate rpm specfiles from gems
Group:          Development/Languages/Ruby
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description -n ruby3.1-rubygem-gem2rpm
Generate source rpms and rpm spec files from a Ruby Gem.
The spec file tries to follow the gem as closely as possible

%package -n ruby3.1-rubygem-gem2rpm-doc
Summary:        RDoc documentation for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       ruby3.1-rubygem-gem2rpm = %{version}

%description -n ruby3.1-rubygem-gem2rpm-doc
Documentation generated at gem installation time.
Usually in RDoc and RI formats.

%post -n ruby3.1-rubygem-gem2rpm
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm         gem2rpm         %{_bindir}/gem2rpm.ruby3.1-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm-%{version}   gem2rpm-%{version}   %{_bindir}/gem2rpm.ruby3.1-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm.ruby3.1 gem2rpm.ruby3.1 %{_bindir}/gem2rpm.ruby3.1-%{version} %{mod_weight}

%preun -n ruby3.1-rubygem-gem2rpm
if [ "$1" = 0 ] ; then
    /usr/sbin/update-alternatives --remove gem2rpm          %{_bindir}/gem2rpm.ruby3.1-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm-%{version}    %{_bindir}/gem2rpm.ruby3.1-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm.ruby3.1  %{_bindir}/gem2rpm.ruby3.1-%{version}
fi

%files -n ruby3.1-rubygem-gem2rpm
%defattr(-,root,root,-)
%{_docdir}/ruby3.1-rubygem-gem2rpm
#{_bindir}/gem2rpm-opensuse
%{_bindir}/gem2rpm.ruby3.1-%{version}
%ghost %{_bindir}/gem2rpm.ruby3.1
%ghost %{_bindir}/gem2rpm-%{version}
%ghost %{_bindir}/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm.ruby3.1
%ghost %{_sysconfdir}/alternatives/gem2rpm-%{version}
# cache file
%{_libdir}/ruby/gems/3.1.0/cache/gem2rpm-%{version}.gem
%{_libdir}/ruby/gems/3.1.0/gems/gem2rpm-%{version}
%{_libdir}/ruby/gems/3.1.0/specifications/gem2rpm-%{version}.gemspec

%if %{with docs}
%files -n ruby3.1-rubygem-gem2rpm-doc
%defattr(-,root,root,-)
%doc %{_libdir}/ruby/gems/3.1.0/doc/gem2rpm-%{version}
%endif
%endif

%if %{with ruby32}
%package -n ruby3.2-rubygem-gem2rpm
Summary:        Generate rpm specfiles from gems
Group:          Development/Languages/Ruby
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description -n ruby3.2-rubygem-gem2rpm
Generate source rpms and rpm spec files from a Ruby Gem.
The spec file tries to follow the gem as closely as possible

%package -n ruby3.2-rubygem-gem2rpm-doc
Summary:        RDoc documentation for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       ruby3.2-rubygem-gem2rpm = %{version}

%description -n ruby3.2-rubygem-gem2rpm-doc
Documentation generated at gem installation time.
Usually in RDoc and RI formats.

%post -n ruby3.2-rubygem-gem2rpm
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm         gem2rpm         %{_bindir}/gem2rpm.ruby3.2-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm-%{version}   gem2rpm-%{version}   %{_bindir}/gem2rpm.ruby3.2-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm.ruby3.2 gem2rpm.ruby3.2 %{_bindir}/gem2rpm.ruby3.2-%{version} %{mod_weight}

%preun -n ruby3.2-rubygem-gem2rpm
if [ "$1" = 0 ] ; then
    /usr/sbin/update-alternatives --remove gem2rpm          %{_bindir}/gem2rpm.ruby3.2-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm-%{version}    %{_bindir}/gem2rpm.ruby3.2-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm.ruby3.2  %{_bindir}/gem2rpm.ruby3.2-%{version}
fi

%files -n ruby3.2-rubygem-gem2rpm
%defattr(-,root,root,-)
%{_docdir}/ruby3.2-rubygem-gem2rpm
#{_bindir}/gem2rpm-opensuse
%{_bindir}/gem2rpm.ruby3.2-%{version}
%ghost %{_bindir}/gem2rpm.ruby3.2
%ghost %{_bindir}/gem2rpm-%{version}
%ghost %{_bindir}/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm.ruby3.2
%ghost %{_sysconfdir}/alternatives/gem2rpm-%{version}
# cache file
%{_libdir}/ruby/gems/3.2.0/cache/gem2rpm-%{version}.gem
%{_libdir}/ruby/gems/3.2.0/gems/gem2rpm-%{version}
%{_libdir}/ruby/gems/3.2.0/specifications/gem2rpm-%{version}.gemspec

%if %{with docs}
%files -n ruby3.2-rubygem-gem2rpm-doc
%defattr(-,root,root,-)
%doc %{_libdir}/ruby/gems/3.2.0/doc/gem2rpm-%{version}
%endif
%endif

%if %{with ruby33}
%package -n ruby3.3-rubygem-gem2rpm
Summary:        Generate rpm specfiles from gems
Group:          Development/Languages/Ruby
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description -n ruby3.3-rubygem-gem2rpm
Generate source rpms and rpm spec files from a Ruby Gem.
The spec file tries to follow the gem as closely as possible

%package -n ruby3.3-rubygem-gem2rpm-doc
Summary:        RDoc documentation for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       ruby3.3-rubygem-gem2rpm = %{version}

%description -n ruby3.3-rubygem-gem2rpm-doc
Documentation generated at gem installation time.
Usually in RDoc and RI formats.

%post -n ruby3.3-rubygem-gem2rpm
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm         gem2rpm         %{_bindir}/gem2rpm.ruby3.3-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm-%{version}   gem2rpm-%{version}   %{_bindir}/gem2rpm.ruby3.3-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm.ruby3.3 gem2rpm.ruby3.3 %{_bindir}/gem2rpm.ruby3.3-%{version} %{mod_weight}

%preun -n ruby3.3-rubygem-gem2rpm
if [ "$1" = 0 ] ; then
    /usr/sbin/update-alternatives --remove gem2rpm          %{_bindir}/gem2rpm.ruby3.3-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm-%{version}    %{_bindir}/gem2rpm.ruby3.3-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm.ruby3.3  %{_bindir}/gem2rpm.ruby3.3-%{version}
fi

%files -n ruby3.3-rubygem-gem2rpm
%defattr(-,root,root,-)
%{_docdir}/ruby3.3-rubygem-gem2rpm
#{_bindir}/gem2rpm-opensuse
%{_bindir}/gem2rpm.ruby3.3-%{version}
%ghost %{_bindir}/gem2rpm.ruby3.3
%ghost %{_bindir}/gem2rpm-%{version}
%ghost %{_bindir}/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm.ruby3.3
%ghost %{_sysconfdir}/alternatives/gem2rpm-%{version}
# cache file
%{_libdir}/ruby/gems/3.3.0/cache/gem2rpm-%{version}.gem
%{_libdir}/ruby/gems/3.3.0/gems/gem2rpm-%{version}
%{_libdir}/ruby/gems/3.3.0/specifications/gem2rpm-%{version}.gemspec

%if %{with docs}
%files -n ruby3.3-rubygem-gem2rpm-doc
%defattr(-,root,root,-)
%doc %{_libdir}/ruby/gems/3.3.0/doc/gem2rpm-%{version}
%endif
%endif

%if %{with ruby34}
%package -n ruby3.4-rubygem-gem2rpm
Summary:        Generate rpm specfiles from gems
Group:          Development/Languages/Ruby
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description -n ruby3.4-rubygem-gem2rpm
Generate source rpms and rpm spec files from a Ruby Gem.
The spec file tries to follow the gem as closely as possible

%package -n ruby3.4-rubygem-gem2rpm-doc
Summary:        RDoc documentation for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       ruby3.4-rubygem-gem2rpm = %{version}

%description -n ruby3.4-rubygem-gem2rpm-doc
Documentation generated at gem installation time.
Usually in RDoc and RI formats.

%post -n ruby3.4-rubygem-gem2rpm
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm         gem2rpm         %{_bindir}/gem2rpm.ruby3.4-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm-%{version}   gem2rpm-%{version}   %{_bindir}/gem2rpm.ruby3.4-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm.ruby3.4 gem2rpm.ruby3.4 %{_bindir}/gem2rpm.ruby3.4-%{version} %{mod_weight}

%preun -n ruby3.4-rubygem-gem2rpm
if [ "$1" = 0 ] ; then
    /usr/sbin/update-alternatives --remove gem2rpm          %{_bindir}/gem2rpm.ruby3.4-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm-%{version}    %{_bindir}/gem2rpm.ruby3.4-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm.ruby3.4  %{_bindir}/gem2rpm.ruby3.4-%{version}
fi

%files -n ruby3.4-rubygem-gem2rpm
%defattr(-,root,root,-)
%{_docdir}/ruby3.4-rubygem-gem2rpm
#{_bindir}/gem2rpm-opensuse
%{_bindir}/gem2rpm.ruby3.4-%{version}
%ghost %{_bindir}/gem2rpm.ruby3.4
%ghost %{_bindir}/gem2rpm-%{version}
%ghost %{_bindir}/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm.ruby3.4
%ghost %{_sysconfdir}/alternatives/gem2rpm-%{version}
# cache file
%{_libdir}/ruby/gems/3.4.0/cache/gem2rpm-%{version}.gem
%{_libdir}/ruby/gems/3.4.0/gems/gem2rpm-%{version}
%{_libdir}/ruby/gems/3.4.0/specifications/gem2rpm-%{version}.gemspec

%if %{with docs}
%files -n ruby3.4-rubygem-gem2rpm-doc
%defattr(-,root,root,-)
%doc %{_libdir}/ruby/gems/3.4.0/doc/gem2rpm-%{version}
%endif
%endif

%if %{with rubinius25}
%package -n rbx2.5-rubygem-gem2rpm
# MANUAL
# /MANUAL
Summary:        Generate rpm specfiles from gems
Group:          Development/Languages/Ruby
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description -n rbx2.5-rubygem-gem2rpm
Generate source rpms and rpm spec files from a Ruby Gem.
The spec file tries to follow the gem as closely as possible.

%package -n rbx2.5-rubygem-gem2rpm-doc
Summary:        RDoc documentation for gem2rpm
Group:          Development/Languages/Ruby
Requires:       rbx2.5-rubygem-gem2rpm = %{version}

%description -n rbx2.5-rubygem-gem2rpm-doc
Documentation generated at gem installation time.
Usually in RDoc and RI formats.

%post -n rbx2.5-rubygem-gem2rpm
/usr/sbin/update-alternatives --install \
    /usr/bin/gem2rpm                      gem2rpm /usr/bin/gem2rpm.rbx2.5-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    /usr/bin/gem2rpm-%{version} gem2rpm-%{version} /usr/bin/gem2rpm.rbx2.5-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    /usr/bin/gem2rpm.rbx2.5     gem2rpm.rbx2.5 /usr/bin/gem2rpm.rbx2.5-%{version} %{mod_weight}

%preun -n rbx2.5-rubygem-gem2rpm
if [ "$1" = 0 ] ; then
    /usr/sbin/update-alternatives --remove gem2rpm /usr/bin/gem2rpm.rbx2.5-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm-%{version} /usr/bin/gem2rpm.rbx2.5-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm.rbx2.5 /usr/bin/gem2rpm.rbx2.5-%{version}
fi

%files -n rbx2.5-rubygem-gem2rpm
%defattr(-,root,root,-)
# MANUAL
# /MANUAL
/usr/share/doc/packages/rbx2.5-rubygem-gem2rpm
%{_bindir}/gem2rpm.rbx2.5-%{version}
%ghost %{_bindir}/gem2rpm.rbx2.5
%ghost %{_bindir}/gem2rpm-%{version}
%ghost %{_bindir}/gem2rpm
%ghost /etc/alternatives/gem2rpm
%ghost /etc/alternatives/gem2rpm.rbx2.5
%ghost /etc/alternatives/gem2rpm-%{version}
# cache file
%{_libdir}/rubinius/gems/2.5/cache/gem2rpm-%{version}.gem
%{_libdir}/rubinius/gems/2.5/gems/gem2rpm-%{version}
%{_libdir}/rubinius/gems/2.5/specifications/gem2rpm-%{version}.gemspec

%if %{with docs}
%files -n rbx2.5-rubygem-gem2rpm-doc
%defattr(-,root,root,-)
%doc %{_libdir}/rubinius/gems/2.5/doc/gem2rpm-%{version}
%endif
%endif
%else
%gem_packages
%endif

%changelog
