#
# spec file for package log4net
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           log4net
Version:        1.2.10
Release:        0
Summary:        A .NET framework for logging
License:        Apache-2.0
Group:          System/Libraries
URL:            http://logging.apache.org/log4net/
Source:         incubating-log4net-1.2.10.zip
Source1:        log4net.key
Source2:        log4net.pc
BuildRequires:  mono-basic
BuildRequires:  mono-data-sqlite
BuildRequires:  mono-devel
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildArch:      noarch
#=============================================================================

%description
log4net is a tool to help the programmer output log statements to a
variety of output targets. log4net is a port of the excellent log4j
framework to the .NET runtime

%prep
%setup -q -c
sed -i "s|@VERSION@|%{version}|" %{SOURCE2}
#=============================================================================

%build
export LC_CTYPE=en_US.UTF-8
cd log4net-%{version}
mcs -out:../log4net.dll \
	-keyfile:%{SOURCE1} \
	/target:library \
	/r:System.dll \
	/r:System.Data.dll \
	/r:System.Web.dll \
	src/Appender/AdoNetAppender.cs \
	src/Appender/AnsiColorTerminalAppender.cs \
	src/Appender/AppenderCollection.cs \
	src/Appender/AppenderSkeleton.cs \
	src/Appender/AspNetTraceAppender.cs \
	src/Appender/BufferingAppenderSkeleton.cs \
	src/Appender/BufferingForwardingAppender.cs \
	src/Appender/ColoredConsoleAppender.cs \
	src/Appender/ConsoleAppender.cs \
	src/Appender/DebugAppender.cs \
	src/Appender/EventLogAppender.cs \
	src/Appender/FileAppender.cs \
	src/Appender/ForwardingAppender.cs \
	src/Appender/IAppender.cs \
	src/Appender/IBulkAppender.cs \
	src/Appender/LocalSyslogAppender.cs \
	src/Appender/MemoryAppender.cs \
	src/Appender/NetSendAppender.cs \
	src/Appender/OutputDebugStringAppender.cs \
	src/Appender/RemoteSyslogAppender.cs \
	src/Appender/RemotingAppender.cs \
	src/Appender/RollingFileAppender.cs \
	src/Appender/SmtpAppender.cs \
	src/Appender/SmtpPickupDirAppender.cs \
	src/Appender/TelnetAppender.cs \
	src/Appender/TextWriterAppender.cs \
	src/Appender/TraceAppender.cs \
	src/Appender/UdpAppender.cs \
	src/Config/AliasDomainAttribute.cs \
	src/Config/AliasRepositoryAttribute.cs \
	src/Config/BasicConfigurator.cs \
	src/Config/ConfiguratorAttribute.cs \
	src/Config/DomainAttribute.cs \
	src/Config/DOMConfigurator.cs \
	src/Config/DOMConfiguratorAttribute.cs \
	src/Config/Log4NetConfigurationSectionHandler.cs \
	src/Config/PluginAttribute.cs \
	src/Config/RepositoryAttribute.cs \
	src/Config/SecurityContextProviderAttribute.cs \
	src/Config/XmlConfigurator.cs \
	src/Config/XmlConfiguratorAttribute.cs \
	src/Core/CompactRepositorySelector.cs \
	src/Core/DefaultRepositorySelector.cs \
	src/Core/ErrorCode.cs \
	src/Core/IAppenderAttachable.cs \
	src/Core/IErrorHandler.cs \
	src/Core/IFixingRequired.cs \
	src/Core/ILogger.cs \
	src/Core/ILoggerWrapper.cs \
	src/Core/IOptionHandler.cs \
	src/Core/IRepositorySelector.cs \
	src/Core/ITriggeringEventEvaluator.cs \
	src/Core/Level.cs \
	src/Core/LevelCollection.cs \
	src/Core/LevelEvaluator.cs \
	src/Core/LevelMap.cs \
	src/Core/LocationInfo.cs \
	src/Core/LogException.cs \
	src/Core/LoggerManager.cs \
	src/Core/LoggerWrapperImpl.cs \
	src/Core/LoggingEvent.cs \
	src/Core/LogImpl.cs \
	src/Core/SecurityContext.cs \
	src/Core/SecurityContextProvider.cs \
	src/Core/WrapperMap.cs \
	src/DateFormatter/AbsoluteTimeDateFormatter.cs \
	src/DateFormatter/DateTimeDateFormatter.cs \
	src/DateFormatter/IDateFormatter.cs \
	src/DateFormatter/Iso8601DateFormatter.cs \
	src/DateFormatter/SimpleDateFormatter.cs \
	src/Filter/DenyAllFilter.cs \
	src/Filter/FilterDecision.cs \
	src/Filter/FilterSkeleton.cs \
	src/Filter/IFilter.cs \
	src/Filter/LevelMatchFilter.cs \
	src/Filter/LevelRangeFilter.cs \
	src/Filter/LoggerMatchFilter.cs \
	src/Filter/MdcFilter.cs \
	src/Filter/NdcFilter.cs \
	src/Filter/PropertyFilter.cs \
	src/Filter/StringMatchFilter.cs \
	src/Layout/Pattern/AppDomainPatternConverter.cs \
	src/Layout/Pattern/DatePatternConverter.cs \
	src/Layout/Pattern/ExceptionPatternConverter.cs \
	src/Layout/Pattern/FileLocationPatternConverter.cs \
	src/Layout/Pattern/FullLocationPatternConverter.cs \
	src/Layout/Pattern/IdentityPatternConverter.cs \
	src/Layout/Pattern/LevelPatternConverter.cs \
	src/Layout/Pattern/LineLocationPatternConverter.cs \
	src/Layout/Pattern/LoggerPatternConverter.cs \
	src/Layout/Pattern/MessagePatternConverter.cs \
	src/Layout/Pattern/MethodLocationPatternConverter.cs \
	src/Layout/Pattern/NamedPatternConverter.cs \
	src/Layout/Pattern/NdcPatternConverter.cs \
	src/Layout/Pattern/PatternLayoutConverter.cs \
	src/Layout/Pattern/PropertyPatternConverter.cs \
	src/Layout/Pattern/RelativeTimePatternConverter.cs \
	src/Layout/Pattern/ThreadPatternConverter.cs \
	src/Layout/Pattern/TypeNamePatternConverter.cs \
	src/Layout/Pattern/UserNamePatternConverter.cs \
	src/Layout/Pattern/UtcDatePatternConverter.cs \
	src/Layout/ExceptionLayout.cs \
	src/Layout/ILayout.cs \
	src/Layout/IRawLayout.cs \
	src/Layout/Layout2RawLayoutAdapter.cs \
	src/Layout/LayoutSkeleton.cs \
	src/Layout/PatternLayout.cs \
	src/Layout/RawLayoutConverter.cs \
	src/Layout/RawPropertyLayout.cs \
	src/Layout/RawTimeStampLayout.cs \
	src/Layout/RawUtcTimeStampLayout.cs \
	src/Layout/SimpleLayout.cs \
	src/Layout/XMLLayout.cs \
	src/Layout/XMLLayoutBase.cs \
	src/Layout/XmlLayoutSchemaLog4j.cs \
	src/ObjectRenderer/DefaultRenderer.cs \
	src/ObjectRenderer/IObjectRenderer.cs \
	src/ObjectRenderer/RendererMap.cs \
	src/Plugin/IPlugin.cs \
	src/Plugin/IPluginFactory.cs \
	src/Plugin/PluginCollection.cs \
	src/Plugin/PluginMap.cs \
	src/Plugin/PluginSkeleton.cs \
	src/Plugin/RemoteLoggingServerPlugin.cs \
	src/Repository/Hierarchy/DefaultLoggerFactory.cs \
	src/Repository/Hierarchy/Hierarchy.cs \
	src/Repository/Hierarchy/ILoggerFactory.cs \
	src/Repository/Hierarchy/Logger.cs \
	src/Repository/Hierarchy/LoggerKey.cs \
	src/Repository/Hierarchy/ProvisionNode.cs \
	src/Repository/Hierarchy/RootLogger.cs \
	src/Repository/Hierarchy/XmlHierarchyConfigurator.cs \
	src/Repository/IBasicRepositoryConfigurator.cs \
	src/Repository/ILoggerRepository.cs \
	src/Repository/IXmlRepositoryConfigurator.cs \
	src/Repository/LoggerRepositorySkeleton.cs \
	src/Util/PatternStringConverters/AppDomainPatternConverter.cs \
	src/Util/PatternStringConverters/DatePatternConverter.cs \
	src/Util/PatternStringConverters/EnvironmentPatternConverter.cs \
	src/Util/PatternStringConverters/IdentityPatternConverter.cs \
	src/Util/PatternStringConverters/LiteralPatternConverter.cs \
	src/Util/PatternStringConverters/NewLinePatternConverter.cs \
	src/Util/PatternStringConverters/ProcessIdPatternConverter.cs \
	src/Util/PatternStringConverters/PropertyPatternConverter.cs \
	src/Util/PatternStringConverters/RandomStringPatternConverter.cs \
	src/Util/PatternStringConverters/UserNamePatternConverter.cs \
	src/Util/PatternStringConverters/UtcDatePatternConverter.cs \
	src/Util/TypeConverters/BooleanConverter.cs \
	src/Util/TypeConverters/ConversionNotSupportedException.cs \
	src/Util/TypeConverters/ConverterRegistry.cs \
	src/Util/TypeConverters/EncodingConverter.cs \
	src/Util/TypeConverters/IConvertFrom.cs \
	src/Util/TypeConverters/IConvertTo.cs \
	src/Util/TypeConverters/IPAddressConverter.cs \
	src/Util/TypeConverters/PatternLayoutConverter.cs \
	src/Util/TypeConverters/PatternStringConverter.cs \
	src/Util/TypeConverters/TypeConverter.cs \
	src/Util/TypeConverters/TypeConverterAttribute.cs \
	src/Util/AppenderAttachedImpl.cs \
	src/Util/CompositeProperties.cs \
	src/Util/ContextPropertiesBase.cs \
	src/Util/CountingQuietTextWriter.cs \
	src/Util/CyclicBuffer.cs \
	src/Util/EmptyCollection.cs \
	src/Util/EmptyDictionary.cs \
	src/Util/FormattingInfo.cs \
	src/Util/GlobalContextProperties.cs \
	src/Util/LevelMapping.cs \
	src/Util/LevelMappingEntry.cs \
	src/Util/LogicalThreadContextProperties.cs \
	src/Util/LogLog.cs \
	src/Util/NativeError.cs \
	src/Util/NullDictionaryEnumerator.cs \
	src/Util/NullEnumerator.cs \
	src/Util/NullSecurityContext.cs \
	src/Util/OnlyOnceErrorHandler.cs \
	src/Util/OptionConverter.cs \
	src/Util/PatternConverter.cs \
	src/Util/PatternParser.cs \
	src/Util/PatternString.cs \
	src/Util/PropertiesDictionary.cs \
	src/Util/ProtectCloseTextWriter.cs \
	src/Util/QuietTextWriter.cs \
	src/Util/ReaderWriterLock.cs \
	src/Util/ReadOnlyPropertiesDictionary.cs \
	src/Util/ReusableStringWriter.cs \
	src/Util/SystemInfo.cs \
	src/Util/SystemStringFormat.cs \
	src/Util/TextWriterAdapter.cs \
	src/Util/ThreadContextProperties.cs \
	src/Util/ThreadContextStack.cs \
	src/Util/ThreadContextStacks.cs \
	src/Util/Transform.cs \
	src/Util/WindowsSecurityContext.cs \
	src/AssemblyInfo.cs \
	src/AssemblyVersionInfo.cs \
	src/GlobalContext.cs \
	src/ILog.cs \
	src/LogicalThreadContext.cs \
	src/LogManager.cs \
	src/MDC.cs \
	src/NDC.cs \
	src/ThreadContext.cs
#=============================================================================

%install
mkdir -p %{buildroot}/%{_datadir}/pkgconfig
cp %{SOURCE2} %{buildroot}/%{_datadir}/pkgconfig
gacutil -package log4net -gacdir %{_prefix}/lib -root %{buildroot}%{_prefix}/lib -i log4net.dll > /dev/null
#=============================================================================

%files
%defattr(755,root,root)
%{_datadir}/pkgconfig/log4net.pc
%{_prefix}/lib/mono/gac
%{_prefix}/lib/mono/log4net

%changelog
