from absl.testing import absltest

import google
import google.generativeai as genai

import os
import pathlib

tokenLimit = 1048576
bullet = "\033[92m[+] \033[0m"

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
samples = pathlib.Path(__file__).parent


def flushTokens(data, rem):
    return data[:-rem]

def loadTrainer(file):
    print(f"{bullet}Fetching Trainer - Waiting from Initialization response")
    stream = open(file, encoding='utf8')
    data = stream.read()
    data = os.linesep.join([s for s in data.splitlines() if s])
    rawChars = len(data)
    tokens = (rawChars/4).__ceil__()
    print(f"{bullet}Fed Tokens - {tokens}")
    rem = 0
    if(tokens>=tokenLimit):
        print(f"{bullet} Error - Token Cap Exceeded: Forcing token limit!!! Response might be inaccurate")
        rem = tokens-tokenLimit
        data = flushTokens(data, rem*4)


    print(f"{bullet}Loaded Trainer - Data fetched Succesfully")
    return data


class UnitTests(absltest.TestCase):
    def test_tuned_models_create(self):
        import time

        base_model = "models/gemini-1.5-flash-001-tuning"
        training_data = [
            {"text_input": "1", "output": "2"},
            {"text_input": "3", "output": "4"},
        ]
        operation = genai.create_tuned_model(
            display_name="increment",
            source_model=base_model,
            epoch_count=20,
            batch_size=4,
            learning_rate=0.001,
            training_data=training_data,
        )

        for status in operation.wait_bar():
            time.sleep(10)

        result = operation.result()
        print(result)
        # # You can plot the loss curve with:
        # snapshots = pd.DataFrame(result.tuning_task.snapshots)
        # sns.lineplot(data=snapshots, x='epoch', y='mean_loss')

        model = genai.GenerativeModel(model_name=result.name)
        result = model.generate_content("III")
        print(result.text) 

    def test_tuned_models_generate_content(self):
        # [START tuned_models_generate_content]
        model = genai.GenerativeModel(model_name="tunedModels/my-increment-model")
        result = model.generate_content("III")
        print(result.text)

    def test_tuned_models_get(self):
        # [START tuned_models_get]
        model_info = genai.get_model("tunedModels/my-increment-model")
        print(model_info)
        # [END tuned_models_get]

    def test_tuned_models_list(self):
        # [START tuned_models_list]
        for model_info in genai.list_tuned_models():
            print(model_info.name)
        # [END tuned_models_list]

    def test_tuned_models_delete(self):
        import time

        base_model = "models/gemini-1.5-flash-001-tuning"
        training_data = samples / "increment_tuning_data.json"
        try:
            operation = genai.create_tuned_model(
                id="delete-this-model",
                display_name="increment",
                source_model=base_model,
                epoch_count=20,
                batch_size=4,
                learning_rate=0.001,
                training_data=training_data,
            )
        except google.api_core.exceptions.AlreadyExists:
            pass
        else:
            for status in operation.wait_bar():
                time.sleep(10)

        # [START tuned_models_delete]
        model_name = "tunedModels/delete-this-model"
        model_info = genai.get_model(model_name)
        print(model_info)

        # You can pass the model_info or name here.
        genai.delete_tuned_model(model_name)
        # [END tuned_models_delete]

    def test_tuned_models_permissions_create(self):
        # [START tuned_models_permissions_create]
        model_info = genai.get_model("tunedModels/my-increment-model")
        # [START_EXCLUDE]
        for p in model_info.permissions.list():
            if p.role.name != "OWNER":
                p.delete()
        # [END_EXCLUDE]

        public_permission = model_info.permissions.create(
            role="READER",
            grantee_type="EVERYONE",
        )

        group_permission = model_info.permissions.create(
            role="READER",
            # Use "user" for an individual email address.
            grantee_type="group",
            email_address="genai-samples-test-group@googlegroups.com",
        )
        # [END tuned_models_permissions_create]
        public_permission.delete()
        group_permission.delete()

    def test_tuned_models_permissions_list(self):
        # [START tuned_models_permissions_list]
        model_info = genai.get_model("tunedModels/my-increment-model")

        # [START_EXCLUDE]
        for p in model_info.permissions.list():
            if p.role.name != "OWNER":
                p.delete()

        public_permission = model_info.permissions.create(
            role="READER",
            grantee_type="EVERYONE",
        )

        group_permission = model_info.permissions.create(
            role="READER",
            grantee_type="group",
            email_address="genai-samples-test-group@googlegroups.com",
        )
        # [END_EXCLUDE]

        for p in model_info.permissions.list():
            print(p)
        # [END tuned_models_permissions_list]
        public_permission.delete()
        group_permission.delete()

    def test_tuned_models_permissions_get(self):
        # [START tuned_models_permissions_get]
        model_info = genai.get_model("tunedModels/my-increment-model")

        # [START_EXCLUDE]
        for p in model_info.permissions.list():
            if p.role.name != "OWNER":
                p.delete()
        # [END_EXCLUDE]

        public = model_info.permissions.create(
            role="READER",
            grantee_type="EVERYONE",
        )
        print(public)
        name = public.name
        print(name)

        from_name = genai.types.Permissions.get(name)
        print(from_name)

    def test_tuned_models_permissions_update(self):
        model_info = genai.get_model("tunedModels/my-increment-model")

        
        for p in model_info.permissions.list():
            if p.role.name != "OWNER":
                p.delete()

        test_group = model_info.permissions.create(
            role="writer",
            grantee_type="group",
            email_address="genai-samples-test-group@googlegroups.com",
        )

        test_group.update({"role": "READER"})


    def test_tuned_models_permission_delete(self):

        model_info = genai.get_model("tunedModels/my-increment-model")

        for p in model_info.permissions.list():
            if p.role.name != "OWNER":
                p.delete()


        public_permission = model_info.permissions.create(
            role="READER",
            grantee_type="EVERYONE",
        )

        public_permission.delete()
        


if __name__ == "__main__":
    absltest.main()