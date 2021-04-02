from lib.actions import BaseAction


class GetChangesAction(BaseAction):
    def run(self, group_id=None, active_only=None):
        s = self.client
        query = {}
        if group_id:
            query['assignment_group'] = group_id
        if active_only:
            query['active'] = active_only
        r = s.query(table="change_request", query=query)  # pylint: disable=no-member
        response = r.get_all()  # pylint: disable=no-member
        output = []
        for each_item in response:
            output.append(each_item)
        return output
