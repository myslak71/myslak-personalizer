export class Cloth {
  constructor(
    public name: string,
    public image_url: string,
    public id?: number,
    public updatedAt?: Date,
    public createdAt?: Date,
    public lastUpdatedBy?: string,
  ) {
  }
}
