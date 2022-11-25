#
# spec file for package rubygem-gem2rpm
#
# Copyright (c) 2022 SUSE LLC
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
%bcond_with     ruby26
%bcond_with     ruby27
%bcond_with     ruby30
%bcond_with     ruby31
%bcond_with     ruby32
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
BuildRequires:  update-alternatives
URL:            https://github.com/lutter/gem2rpm/
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml.documentation
Source2:        gem2rpm-opensuse
Source3:        series
Patch01:        0001-use-the-ID-from-os-release-to-use-the-proper-templat.patch
Patch02:        0002-added-basic-config-file-support-to-gem2rpm-in-yaml-f.patch
Patch03:        0003-new-opensuse-templates.-they-require-the-config-file.patch
Patch04:        0004-added-example-gem2rpm.yml.patch
Patch05:        0005-properly-shorten-description-and-summary.patch
Patch06:        0006-Preserve-the-license-header-found-in-the-output-file.patch
Patch07:        0007-fixes-for-the-opensuse-template.patch
Patch08:        0008-do-not-use-not-.-not-supported-on-1.8-e.g.patch
Patch09:        0009-No-longer-require-the-ruby-version-inside-the-subpac.patch
Patch10:        0010-Try-to-load-rbconfigpackagingsupport-and-fail-gracef.patch
Patch11:        0011-Add-support-for-scripts-pre-post-for-subpackages.patch
Patch12:        0012-typo-in-gem2rpm.yml.documentation-custom_pkgs-instea.patch
Patch13:        0013-Also-tag-LICENSE-MIT-as-docfile.patch
Patch14:        0014-Refactor-into-multiple-lines.patch
Patch15:        0015-Add-licence-to-the-list-of-license-files-as-well.patch
Patch16:        0016-add-two-more-ways-to-express-changes.patch
Patch17:        0017-.markdown-is-also-seen-in-the-wild.patch
Patch18:        0018-Only-use-the-extensions-doc-dir-on-MRI-2.1.x.patch
Patch19:        0019-Cleaner-solution-for-the-extensions-doc-dir.patch
Patch20:        0020-Ruby-1.8-insists-on-the-for-the-parameter.patch
Patch21:        0021-Fix-company-name-in-copyright-header.patch
Patch22:        0022-add-the-touch-for-build-compare-to-the-template.patch
Patch23:        0023-Also-tag-APACHE-LICENSE-2.0-as-docfile.patch
Patch24:        0024-add-ability-to-provide-alternative-main-Source.patch
Patch25:        0025-allow-running-commands-after-patching.patch
Patch26:        0026-use-https-instead-of-http-for-rubygems.org.patch
Patch27:        0027-quote-version_suffix-in-gem2rpm.yml.documentation-to.patch
Patch28:        0028-add-binary_map-support.patch
Patch29:        0029-Use-or-for-the-conditions-instead-of-and.patch
Patch30:        0030-gem_package.spec.erb-sync-with-ruby-common.patch
Patch31:        0031-use-template-opensuse-on-openSUSE-Tumbleweed-where-e.patch
Patch32:        0032-Replace-no-rdoc-no-ri-with-no-document.patch
Patch128:       template_loader.patch
Summary:        Generate rpm specfiles from gems
License:        GPL-2.0-or-later
Group:          Development/Languages/Ruby
Requires(post): update-alternatives
Requires(preun):update-alternatives

%description
Generate source rpms and rpm spec files from a Ruby Gem.
The spec file tries to follow the gem as closely as possible

%prep
%gem_unpack
%patch01 -p1
%patch02 -p1
%patch03 -p1
%patch04 -p1
%patch05 -p1
%patch06 -p1
%patch07 -p1
%patch08 -p1
%patch09 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch128 -p1

%build
perl -p -i -e 's|("templates/opensuse.spec.erb".freeze)|$1, "templates/gem_packages.spec.erb".freeze|g' *gemspec
%gem_build

%install
%gem_install -f --no-rdoc --no-ri --symlink-binaries --doc-files="AUTHORS LICENSE README"
for i in %{buildroot}%{_docdir}/*rubygem-gem2rpm*/ ; do
  install -m 0644 %{S:1} $i/gem2rpm.yml
done

%if %{with gem2rpm_bootstrap}
%if %{with ruby21}
%package -n ruby2.1-rubygem-gem2rpm
Summary:        Generate rpm specfiles from gems
Group:          Development/Languages/Ruby
Requires(post): update-alternatives
Requires(preun):update-alternatives

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
Requires(preun):update-alternatives

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
Requires(preun):update-alternatives

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
Requires(preun):update-alternatives

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
Requires(preun):update-alternatives

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
Requires(preun):update-alternatives

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
Requires(preun):update-alternatives

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
Requires(preun):update-alternatives

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
Requires(preun):update-alternatives

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
Requires(preun):update-alternatives

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
Requires(preun):update-alternatives

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
Requires(preun):update-alternatives

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
Requires(preun):update-alternatives

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
%{_libdir}/ruby/gems/3.2.0+3/cache/gem2rpm-%{version}.gem
%{_libdir}/ruby/gems/3.2.0+3/gems/gem2rpm-%{version}
%{_libdir}/ruby/gems/3.2.0+3/specifications/gem2rpm-%{version}.gemspec

%if %{with docs}
%files -n ruby3.2-rubygem-gem2rpm-doc
%defattr(-,root,root,-)
%doc %{_libdir}/ruby/gems/3.2.0+3/doc/gem2rpm-%{version}
%endif
%endif

%if %{with rubinius25}
%package -n rbx2.5-rubygem-gem2rpm
# MANUAL
# /MANUAL
Summary:        Generate rpm specfiles from gems
Group:          Development/Languages/Ruby
Requires(post): update-alternatives
Requires(preun):update-alternatives

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
