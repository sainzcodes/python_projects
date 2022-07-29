public class Tree {
	double heightFT;
	double trunkDiamaterInches;
	TreeType treeType;

	void grow() {
		this.heightFT = this.heightFT + 10;
		this.trunkDiamaterInches = this.trunkDiamaterInches + 1;
	}
}
