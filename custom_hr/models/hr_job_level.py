from odoo import models, fields, _

class HrJobLevel(models.Model):
    """
    Store Hr Level
    """
    _name = 'hr.job.level'
    _description = 'Hr Level'
    
    name = fields.Char('Job level', required=True)
    description = fields.Char('Description')
    level_no = fields.Integer('Level No')
    turn_around_time = fields.Float('Turn-Around Time')
    
    
    
    _sql_constraints = [
        ('check_turn_around_time', 'CHECK(turn_around_time >= 0)', 'The Turn-Around Time should be positive.'),
        ('check_level_no', 'CHECK(level_no >= 0)', 'Level No should be positive.'),
    ]
    
    def copy(self, default=None):
        default = dict(default or {})
        default['name'] = self.name + ' (copy)'
        return super().copy(default)
