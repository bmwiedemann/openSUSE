<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="xml" encoding="UTF-8" indent="yes"/>

<xsl:template match="/">

<xsl:comment>
                This file is generated,
                don't manually modify this file,
                please check README
</xsl:comment>

<xsl:comment> OBS-AddTag: <xsl:value-of select="param/name" />:v%PKG_VERSION%-rev&lt;VERSION&gt; <xsl:value-of select="param/name" />:v%PKG_VERSION%-rev&lt;VERSION&gt;-build&lt;RELEASE&gt; </xsl:comment>

<image schemaversion="6.9" name="csi-livenessprobe-image" xmlns:suse_label_helper="com.suse.label_helper">
  <description type="system">
    <author>SUSE Containers Team</author>
    <contact>containers@suse.com</contact>
    <specification>csi-livenessprobe running on a <xsl:value-of select="param/os" /> container guest</specification>
  </description>
  <preferences>
    <type image="docker">
      <xsl:attribute name="derived_from">
        <xsl:value-of select="param/image" />
      </xsl:attribute>
      <containerconfig
        tag="v%PKG_VERSION%"
        maintainer="SUSE Containers Team &lt;containers@suse.com&gt;"
        >
        <xsl:attribute name="name">
          <xsl:value-of select="param/name" />
        </xsl:attribute>
        
        <entrypoint execute="/usr/bin/livenessprobe"/>
        <subcommand clear="true"/>
        <labels>
          <suse_label_helper:add_prefix>
            <xsl:attribute name="prefix">
              <xsl:value-of select="param/prefix" />
            </xsl:attribute>
          
            <label name="org.opencontainers.image.description">
              <xsl:attribute name="value">csi-livenessprobe running on a <xsl:value-of select="param/os" /> container guest</xsl:attribute>
            </label>
            <label name="org.opencontainers.image.title">
              <xsl:attribute name="value">
                <xsl:value-of select="param/title" />
              </xsl:attribute>
            </label>
            <label name="org.opencontainers.image.created" value="%BUILDTIME%"/>
            <label name="org.opencontainers.image.vendor" value="SUSE LLC"/>
            <label name="org.opencontainers.image.url">
              <xsl:attribute name="value">
                <xsl:value-of select="param/url" />
              </xsl:attribute>
            </label>
            <label name="org.opencontainers.image.version" value="v%PKG_VERSION%"/>
            <label name="org.openbuildservice.disturl" value="%DISTURL%"/>
            <label>
              <xsl:attribute name="name">
                <xsl:value-of select="param/referencelabel" />
              </xsl:attribute>
              <xsl:attribute name="value">
                <xsl:value-of select="param/reference" />
              </xsl:attribute>
            </label>
          </suse_label_helper:add_prefix>
        </labels>
      </containerconfig>
    </type>
    <version>1</version>
    <packagemanager>zypper</packagemanager>
    <rpm-excludedocs>true</rpm-excludedocs>
  </preferences>
  <repository>
    <source path="obsrepositories:/"/>
  </repository>
  <packages type="image">
    <package name="csi-livenessprobe"/>
  </packages>

  <xsl:if test="param/packages_boot">
    <packages type='bootstrap'>

      <xsl:for-each select="param/packages_boot/package">
        <package>
          <xsl:attribute name="name">
            <xsl:value-of select="name" />
          </xsl:attribute>
        </package>
      </xsl:for-each>

    </packages>
  </xsl:if>

</image>

</xsl:template>

</xsl:stylesheet>
