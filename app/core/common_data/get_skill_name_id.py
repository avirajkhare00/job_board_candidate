from app.models import PrimarySkills, SecondarySkills, UserGeneratedSkills


class GetSkillNameId:

    def __init__(self, skill_id):

        self.skill_id = skill_id
        self.skill_category = self.skill_id.split('_')[0]
        self.skill_id_int = int(self.skill_id.split('_')[1])

    def get_skill_name(self):

        if self.skill_category == 'ps':

            if PrimarySkills.objects.filter(primary_skill_id=self.skill_id_int).exists():

                skill = PrimarySkills.objects.get(primary_skill_id=self.skill_id_int)

                return {
                    'status': 'ok',
                    'type': 'primary',
                    'skill_id': skill.primary_skill_id,
                    'skill_name': skill.name
                }

            else:

                return {
                    'status': 'not_found'
                }

        if self.skill_category == 'ss':

            if SecondarySkills.objects.filter(secondary_skill_id=self.skill_id_int).exists():

                skill = SecondarySkills.objects.get(secondary_skill_id=self.skill_id_int)

                return {
                    'status': 'ok',
                    'type': 'secondary',
                    'skill_id': skill.secondary_skill_id,
                    'skill_name': skill.name
                }

            else:

                return {
                    'status': 'not_found'
                }

        if self.skill_category == 'us':

            if UserGeneratedSkills.objects.filter(skill_id=self.skill_id_int).exists():

                skill = UserGeneratedSkills.objects.get(skill_id=self.skill_id_int)

                return {
                    'status': 'ok',
                    'type': 'user',
                    'skill_id': skill.skill_id,
                    'skill_name': skill.name
                }

            else:

                return {
                    'status': 'not_found'
                }
