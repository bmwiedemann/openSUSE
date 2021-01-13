/*
   SPDX-FileCopyrightText: 2020-2021 Fabian Vogt <fabian@ritter-vogt.de>
   SPDX-License-Identifier: GPL-3.0-or-later
*/

#include <cstdio>
#include <cstdlib>

#include <dlfcn.h>

#include <QGuiApplication>
#include <QPluginLoader>
#include <QQmlExtensionPlugin>
#include <QDebug>
#include <QFileInfo>
#include <QQmlError>

#include <QtQml/private/qqmlmetatype_p.h>
#include <QtQml/private/qhashedstring_p.h>

/* Some of the overridden functions here are called before static initialization
 * of this object is done, so use a function-local static variable instead, which
 * is initialized on the first call. */
static QHash<QPair<QString,int>, int> &importDatabase()
{
        static QHash<QPair<QString,int>, int> importDatabase;
        return importDatabase;
}

/* Add the specific import to the database, keeping the highest minor version for
 * each identifier + major version. */
static void foundImportVersion(const QString &import, int versionMajor, int versionMinor)
{
	qDebug() << "Found" << import << versionMajor << versionMinor;

	auto &moduleVersion = importDatabase()[{import, versionMajor}];
	if(moduleVersion < versionMinor)
		moduleVersion = versionMinor;
}

/* Catch calls to qmlRegisterModule, the information is not reachable any other way... */
void qmlRegisterModule(const char *uri, int versionMajor, int versionMinor)
{
//	qDebug() << uri << versionMajor << versionMinor;

	foundImportVersion(uri, versionMajor, versionMinor);

	if(auto *a = dlsym(RTLD_NEXT, "_Z17qmlRegisterModulePKcii"))
	{
		auto c = (decltype(&qmlRegisterModule))a;
		return c(uri, versionMajor, versionMinor);
	}
}

#if QT_VERSION >= QT_VERSION_CHECK(6, 0, 0)
/* Catch calls to QQmlModuleRegistration and trigger registration immediately. */
void QQmlMetaType::qmlInsertModuleRegistration(const QString &uri, void (*registerFunction)())
{
	registerFunction();

	if(auto *a = dlsym(RTLD_NEXT, "_ZN12QQmlMetaType27qmlInsertModuleRegistrationERK7QStringPFvvE"))
	{
		auto c = (decltype(&QQmlMetaType::qmlInsertModuleRegistration))a;
		return c(uri, registerFunction);
	}
}
#else
/* Catch calls to QQmlModuleRegistration and trigger registration immediately. */
void QQmlMetaType::qmlInsertModuleRegistration(const QString &uri, int majorVersion,
                                               void (*registerFunction)())
{
	registerFunction();

	if(auto *a = dlsym(RTLD_NEXT, "_ZN12QQmlMetaType27qmlInsertModuleRegistrationERK7QStringiPFvvE"))
	{
		auto c = (decltype(&QQmlMetaType::qmlInsertModuleRegistration))a;
		return c(uri, majorVersion, registerFunction);
	}
}
#endif

int main(int argc, char *argv[])
{
	// Also used by qmlplugindump
	setenv("QT_QPA_PLATFORM", "minimal", 0);

	QGuiApplication app(argc, argv);
	QPluginLoader loader(app.arguments().at(1));
	auto *a = loader.instance();
	if(!a)
	{
		qCritical() << loader.errorString();
		return 1;
	}

	QString typeNamespace = app.arguments().at(2);
	QList<QQmlError> list;
	/* Using this private call is more flexible (deals with various types of plugins)
	 * and also sets up more internal state like baseUrl, which is required by some. */
	QQmlMetaType::registerPluginTypes(a, QFileInfo(app.arguments().at(1)).absolutePath(), app.arguments().at(2), typeNamespace, {}, &list);

	// Iterate all known types and note their module identifier + version
	for(auto type : QQmlMetaType::qmlAllTypes())
	{
//		qDebug() << type.module() << type.typeName() << type.majorVersion() << type.minorVersion();
#if QT_VERSION >= QT_VERSION_CHECK(6, 0, 0)
		foundImportVersion(type.module(), type.version().majorVersion(), type.version().minorVersion());
#else
		foundImportVersion(type.module(), type.majorVersion(), type.minorVersion());
#endif
	}

	// Print the database in a parsable format
	for(auto i = importDatabase().constBegin(); i != importDatabase().constEnd(); ++i)
		printf("%s.%d %d\n", qPrintable(i.key().first), i.key().second, i.value());
}
