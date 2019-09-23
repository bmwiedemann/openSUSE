<?xml version='1.0' encoding='utf-8' ?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0" xmlns:y="http://www.suse.com/1.0/yast2ns">
  <xsl:output method="text"/>

  <xsl:template match="/">
    <xsl:text>#!/bin/sh
</xsl:text>

    <xsl:for-each select="y:productDefines/y:software/y:extra_urls/y:extra_url">
      <xsl:text>zypper addrepo</xsl:text>
      <!-- disabled if not set -->
      <xsl:if test="not(y:enabled = 'true')">
        <xsl:text> --disable</xsl:text>
      </xsl:if>
      <xsl:if test="y:autorefresh = 'true'">
        <xsl:text> --refresh</xsl:text>
      </xsl:if>
      <xsl:if test="y:priority">
          <xsl:text> -p </xsl:text><xsl:value-of select="y:priority"/>
      </xsl:if>
      <xsl:text> --name '</xsl:text>
      <xsl:value-of select="y:name"/>
      <xsl:text>' '</xsl:text>
      <xsl:value-of select="y:baseurl"/>
      <xsl:if test="y:prod_dir != '/'"><xsl:value-of select="y:prod_dir"/></xsl:if>
      <xsl:text>' '</xsl:text><xsl:value-of select="y:alias"/>
      <xsl:text>';
</xsl:text>
    </xsl:for-each>
  </xsl:template>
</xsl:stylesheet>

