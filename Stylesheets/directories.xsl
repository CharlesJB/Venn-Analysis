<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:include href="join.xsl"/>

<xsl:template match="/analysis">
	<xsl:for-each select="venn">
		( mkdir -p results/$(basename 
		<xsl:call-template name="join">
			<xsl:with-param name="list" select="sample"/>
			<xsl:with-param name="separator" select="')_$(basename '"/>
		</xsl:call-template>
		));
	</xsl:for-each>
</xsl:template>
</xsl:stylesheet>
