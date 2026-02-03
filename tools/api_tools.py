"""Generated API tools: register_tools(mcp) to attach all tools."""

def register_tools(mcp):
    from core import api_client

    @mcp.tool()
    def ActionItem_Reports(portfolioGuid) -> dict:
        """Get the list of all available Reports for ActionItems"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/actionitems/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ActionItem_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for ActionItems"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/actionitems/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ActionItem_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of ActionItem Records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/actionitems", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ActionItem_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of ActionItem Records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/actionitems/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ActionItem_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of ActionItem Records, including all children, based on a query request"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/actionitems/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ActionItem_Post(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates Individual ActionItem"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/actionitems", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ActionItem_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of ActionItem Records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/actionitems/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ActionItem_SubmitWorkflowResponse(portfolioGuid, projectId, body=None) -> dict:
        """Submits a workflow response for an Action item"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/actionitems/submitWorkflowResponse", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ActionItem_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get Workflow states to be used in ActionItems"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/actionitems/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ActionItem_GetWorkflowTemplates(portfolioGuid, projectId) -> dict:
        """Get Workflow templates for Action item records that can be used to create new records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/actionitems/workflowtemplates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ActionItem_GetByID(portfolioGuid, projectId, actionItemId) -> dict:
        """Get Individual ActionItem Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "actionItemId": actionItemId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/actionitems/{actionItemId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Budget_Reports(portfolioGuid) -> dict:
        """Get list of all available Reports for Budget"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/budgets/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Budget_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for Budget"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/budgets/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Budget_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of Budget records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/budgets", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Budget_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of Budget records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/budgets/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Budget_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of Budget records (including all children) based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/budgets/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Budget_Post(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates Individual Budget"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/budgets", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Budget_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of Budget records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/budgets/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Budget_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get WorkflowStates for Budget Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/budgets/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Budget_GetByID(portfolioGuid, projectId, budgetId) -> dict:
        """Get Individual Budget Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "budgetId": budgetId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/budgets/{budgetId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ChangeOrderRequest_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for ChangeOrderRequest"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/changeOrderRequests/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ChangeOrderRequest_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for ChangeOrderRequest"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/changeOrderRequests/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ChangeOrderRequest_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of ChangeOrderRequest records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/changeOrderRequests", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ChangeOrderRequest_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of ChangeOrderRequest records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/changeOrderRequests/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ChangeOrderRequest_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of ChangeOrderRequest records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/changeOrderRequests/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def ChangeOrderRequest_Post(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates Individual ChangeOrderRequest"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/changeOrderRequests", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Checklist_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of CheckList Records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/checklists/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Checklist_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of CheckList Records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/checklists/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Checklist_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of CheckList Records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/checklists/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Checklist_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get WorkflowStates for CheckList Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/checklists/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Contract_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for Contract"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/contracts/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Contract_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for Contract"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/contracts/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Contract_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of Contract records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/contracts/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def Contract_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of Contract records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/contracts/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DailyReport_Reports(portfolioGuid) -> dict:
        """Get list of all available reports for DailyReport"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/dailyreports/reports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DailyReport_UDFs(portfolioGuid) -> dict:
        """Get list of all available UDFs for DailyReport"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/dailyreports/udfs", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DailyReport_List(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of DailyReport records, including all children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/dailyreports", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DailyReport_ListOnlyWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of DailyReport records based on a query request which can optionally specify which children to retrieve"""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/dailyreports/list", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DailyReport_ListWithQuery(portfolioGuid, body=None) -> dict:
        """Get Collection of DailyReport records, including all children, based on a query request."""
        path_params = {"portfolioGuid": portfolioGuid}
        query_params = None
        result = api_client.call("/{portfolioGuid}/dailyreports/query", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DailyReport_Post(portfolioGuid, projectId, body=None) -> dict:
        """Creates/Updates Individual DailyReport"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/dailyreports", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DailyReport_ListOnly(portfolioGuid, projectId, offset=None, limit=None) -> dict:
        """Get Collection of DailyReport records, not including their children."""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"offset": offset, "limit": limit}
        result = api_client.call("/{portfolioGuid}/{projectId}/dailyreports/list", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DailyReport_SubmitWorkflowResponse(portfolioGuid, projectId, body=None) -> dict:
        """Submits a workflow response for a DailyReport"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/dailyreports/submitWorkflowResponse", "POST", path_params=path_params, query_params=query_params, body=body)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DailyReport_GetWorkflowStates(portfolioGuid, projectId, dtLastSyncDateTime=None) -> dict:
        """Get WorkflowStates for DailyReport Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = {"dtLastSyncDateTime": dtLastSyncDateTime}
        result = api_client.call("/{portfolioGuid}/{projectId}/dailyreports/workflowstates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DailyReport_GetWorkflowTemplates(portfolioGuid, projectId) -> dict:
        """Get Workflow templates for Daily report records that can be used to create new records"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/dailyreports/workflowtemplates", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result
    @mcp.tool()
    def DailyReport_GetByID(portfolioGuid, projectId, dailyReportId) -> dict:
        """Get Individual DailyReport Record"""
        path_params = {"portfolioGuid": portfolioGuid, "projectId": projectId, "dailyReportId": dailyReportId}
        query_params = None
        result = api_client.call("/{portfolioGuid}/{projectId}/dailyreports/{dailyReportId}", "GET", path_params=path_params, query_params=query_params, body=None)
        if result.get("isError"):
            return result
        return result