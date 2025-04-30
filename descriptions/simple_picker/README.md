`git lfs pull` to download mesh files first

You can generate webots proto by following commands. For more details, please refer to [cyberbotics/urdf2webots](https://github.com/cyberbotics/urdf2webots).

`python -m urdf2webots.importer --input=picker.urdf`

or more details:

```bash
poetry run python -m urdf2webots.importer --input=picker_fine.urdf --output=build/picker.proto
cp -r build/* ~/Documents/webots_tutor/protos/
```

You may need to modify `files:/meshes/*dae` file path in generated proto file first before you copy to detination.

```bash
sed -i "s|../file:|${PWD}|g" build/picker.proto
```
